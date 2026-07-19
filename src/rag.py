import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_ai_playlist(user_profile, user_songs):
    prompt = f"""
    This user is on a plane and needs a playlist for the journey. This is their user profile, detailing their music preferences and mood:
    {user_profile}

    Based on this profile, we have recommended the following songs using a traditional recommendation algorithm:
    {user_songs}

    Based on the recommended songs, please reorder them in a way that would best suit the user's journey on the plane.

    The ordering must adapt to the user’s musical preferences, genres, listening habits, and desired mood. Do not assume that every listener wants an energetic takeoff, a calm cruise, or a soft ending.

    Create a coherent progression using these principles:

    1. **Welcoming opening:** Start with a track that feels accessible and appropriate for the listener. This could be familiar, energetic, calming, atmospheric, or emotionally engaging.

    2. **Natural development:** Let the next few tracks build on the opening in a way that suits the music. The progression may increase, decrease, or maintain intensity depending on the listener’s preferences.

    3. **Engaging middle:** Keep the central part of the playlist interesting through appropriate variation in mood, tempo, rhythm, instrumentation, vocals, genre, or texture. For highly consistent genres such as lo-fi or ambient, use subtle variation rather than dramatic changes.

    4. **Intentional contrast:** Avoid placing too many nearly identical tracks together, but do not introduce contrast merely for the sake of variety. Any change should feel musically natural.

    5. **Satisfying conclusion:** End with a track that provides a sense of completion for that particular listener. The ending may be calming, uplifting, energetic, reflective, cinematic, or open-ended.

    Prioritize:

    * The user’s musical taste and requested mood
    * Smooth or intentional transitions
    * A coherent overall progression
    * Enough variation to avoid repetition
    * A strong opening and satisfying ending

    Do not force the playlist into a fixed boarding, takeoff, cruise, and landing energy pattern. Use the phases of the flight only as context when they improve the experience.

    Do not assume that higher energy is better. Interpret “energy” relative to the genre. For example, meaningful variation in lo-fi may involve subtle changes in warmth, rhythm, instrumentation, or atmosphere, while variation in pop or rock may involve more noticeable changes in intensity.

    Avoid more than three tracks in a row that are extremely similar in mood, energy, tempo, or production, unless consistency is clearly part of the user’s requested experience.

    For each song, briefly explain:

    1. Why it belongs in that position
    2. How it connects with the previous and next tracks
    3. What role it plays in the playlist’s overall progression

    Please do not write more than 2 medium sized sentences per song explanation.

    At the end, summarize the playlist’s progression in one sentence and explain how the ordering reflects the user’s preferences.
    
    Please provide the reordered list of songs along with the explanations in a clear and concise manner, and avoid any jargon. Make the explanation engaging and informative, but brief. 
    
    Make sure to only include songs that are in the original recommended list and DO NOT add any new songs. Also DO NOT remove any songs from the original list, just reorder them based on the user's journey on the plane.

    Also, do not write anything before the list of songs and explanations. Just start with the first song and its explanation. The format should be as follows:
    1. Song Title - Artist Name: Explanation for why this song is recommended in this order.
    (include newline between each song for readability)
    2. Song Title - Artist Name: Explanation for why this song is recommended in this order.
    ...
    10. Song Title - Artist Name: Explanation for why this song is recommended in this order.
    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text


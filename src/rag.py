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

    Based on the recommended songs, please reorder them in a way that would best suit the user's journey on the plane. For each song, provide a one-liner explanation for why it is recommended in that order and how it fits the user's journey. The explanation should consider the user's mood, energy levels, and the overall vibe of the flight. 
    
    Please provide the reordered list of songs along with the explanations in a clear and concise manner, and avoid any jargon. Make the explanation engaging and informative, but brief. 
    
    Make sure to only include songs that are in the original recommended list and DO NOT add any new songs. Also DO NOT remove any songs from the original list, just reorder them based on the user's journey on the plane.

    Also, do not write anything before the list of songs and explanations. Just start with the first song and its explanation. The format should be as follows:
    1. Song Title - Artist Name: Explanation for why this song is recommended in this order.
    (include newline between each song for readability)
    2. Song Title - Artist Name: Explanation for why this song is recommended in this order.
    ...
    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text


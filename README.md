# TravelTune AI: RAG-Enhanced Music Recommender

## Base Project and Original Scope
This project is an extension of my original Music Recommender Simulation (Project 3). Originally, this project used a traditional recommendation algorithm to score songs from a local dataset using the user's music preferences (specifically mood, genre, energy, danceability, and valence). It ranked songs based on the user's preferences and returned the top k recommended matches with basic score-based explanations.

---

## Title and Summary
TravelTune AI is a personalized playlist generator designed to create a plane ride music playlist. It enhances the original traditional recommender system with Retrieval-Augmented Generation (RAG).

Instead of only returning ranked songs, the system first retrieves the top matching songs from the local dataset, then uses Gemini AI to reorder the songs into a better listening journey specifically for a flight and explain why each song fits the user’s mood, energy level, and travel context.

This matters because recommendations become more human, contextual, and engaging rather than just numeric rankings.

---

## Architecture Overview

The system has three main layers:

1. Traditional Recommendation Engine  
Loads the song dataset, gets user music profile input, filters poor matches, computes weighted scores, and returns the top K recommendations.

2. RAG + AI Layer  
The retrieved songs and user profile are passed into Gemini AI (retrieval). Gemini reorders the playlist for a smoother travel experience and explains why each song belongs in that position (augmented generation). Gemini output is printed for the user to see.

3. Reliability Layer  
If the Gemini API call fails, the system uses a try/except fallback and safely prints the original ranked recommendations.

More comprehensive overview:
The user begins by providing music preferences such as mood, favorite genres, and desired energy level.

The system then loads the local song dataset and evaluates each song one by one. Songs that fail basic valence filters are discarded. Songs that pass are scored using factors (mood, genre, energy, and danceability).

All valid songs are ranked, and the top K songs are retrieved.

Those retrieved songs, along with the user profile and travel scenario, are sent to Gemini AI as context. Gemini generates a reordered playlist and explains the reasoning for each song.

If the AI call succeeds, the AI playlist is shown to the user. If the AI call fails, the system falls back to the original ranked recommendations.

This creates a complete pipeline of input → retrieval → AI reasoning → output, with built-in reliability checks.

---

## Setup Instructions

1. Clone the repository
git clone <your_repo_url>
cd project_folder

2. Create a virtual environment
python -m venv venv
source venv/bin/activate

3. Install dependencies
pip install google-genai
pip install python-dotenv

4. Create a .env file and add these lines to it:
GEMINI_API_KEY=your_api_key_here

5. Create .gitignore file and add these lines to it:
__pycache__/
.env

6. Run the project
python3 src/main.py

---

## Sample Interactions

### Example 1

Input User Profile:
High Energy Pop

Retrieved Songs:
1. Sunrise City
   Score: 0.98
2. Levitating
   Score: 0.98
3. Rooftop Lights
   Score: 0.98
4. As It Was
   Score: 0.58
5. Pink Venom
   Score: 0.57
6. Midnight Coding
   Score: 0.57
7. Focus Flow
   Score: 0.56
8. Library Rain
   Score: 0.55
9. Gym Hero
   Score: 0.55
10. Spacewalk Thoughts
   Score: 0.52

AI Output:
1. Levitating - Dua Lipa: Kick off your flight with this incredibly happy and energetic pop hit, perfect for getting you in a great mood as you board and prepare for takeoff.
2. Sunrise City - Neon Echo: Keep the good vibes soaring with another upbeat pop track, ideal for a cheerful start to your journey as you leave the ground behind.
3. Rooftop Lights - Indigo Parade: Continue the happy, energetic pop atmosphere, making your initial climb a bright and enjoyable experience.
4. Pink Venom - BLACKPINK: As you reach cruising altitude, let this energetic K-pop track keep your spirits high with its danceable beat, perfect for feeling awake and engaged.
5. Gym Hero - Max Pulse: This high-energy pop track is great for a mid-flight boost if you're feeling a bit sluggish, keeping you energized and upbeat.
6. As It Was - Harry Styles: Settle into the cruising phase with this popular pop song; it’s a familiar, steady rhythm that's great for relaxed listening or looking out the window.
7. Midnight Coding - LoRoom: Transition into a more relaxed segment of your flight with this chill track, perfect for focusing on a book, work, or simply unwinding.
8. Focus Flow - LoRoom: Maintain a calm and centered mood with this focused track, ideal for quiet concentration or just enjoying a peaceful moment in the air.
9. Library Rain - Paper Lanterns: For deeper relaxation or if you’re trying to rest, this very chill track provides a soothing backdrop during your flight.
10. Spacewalk Thoughts - Orbit Bloom: Wind down completely with this ambient, chill track, perfect for the final stages of the flight as you prepare for landing in a calm state.

---

### Example 2

Input User Profile:
Sad Gym Junkie

Retrieved Songs:
1. Storm Runner
   Score: 1.00
2. Night Drive Loop
   Score: 0.85
3. Fix You
   Score: 0.76
4. Back to December
   Score: 0.53
5. The Night We Met
   Score: 0.53
6. Someone Like You
   Score: 0.51

AI Output:
1. Storm Runner - Voltline: Kicking off your journey with an intense rock track, perfect for fueling your energy as the plane takes flight.
2. Night Drive Loop - Neon Echo: Settling into the flight with this moody synthwave tune, ideal for gazing out the window during the smooth cruise.
3. Fix You - Coldplay: A slightly more reflective rock song that matches your preferred genre while easing into a thoughtful, calm mood mid-flight.
4. Back to December - Taylor Swift: This mellow and emotional track provides a gentle, sad vibe, great for some quiet introspection during the longer stretch of the journey.
5. The Night We Met - Lord Huron: Continuing the reflective mood, this song offers a calming, dreamy atmosphere as you unwind further into your journey.
6. Someone Like You - Adele: A profoundly emotional and low-energy track to softly conclude your playlist, perfect for a peaceful descent or quiet contemplation before landing.

---

### Example 3

Input User Profile:
Chill Lofi

Retrieved Songs:
1. Spacewalk Thoughts
   Score: 0.98
2. Library Rain
   Score: 0.98
3. Midnight Coding
   Score: 0.96
4. Coffee Shop Stories
   Score: 0.86
5. Focus Flow
   Score: 0.85
6. Weightless
   Score: 0.55
7. Bad Guy
   Score: 0.31
8. As It Was
   Score: 0.28
9. Takedown
   Score: 0.23
10. Pink Venom
   Score: 0.23

AI Output:
1. Weightless - Marconi Union: This deeply ambient track is perfect for the initial calm of boarding and the serene feeling of taking off, helping you relax into the journey.
2. Spacewalk Thoughts - Orbit Bloom: Continue your ascent with this dreamy ambient tune, ideal for watching the clouds drift by and settling into the sky-high experience.
3. Library Rain - Paper Lanterns: Settle into cruising altitude with this comforting lofi track, perfect for background listening, reading, or quiet reflection.
4. Coffee Shop Stories - Slow Stereo: Enjoy a sophisticated, relaxed jazz vibe as you sip a beverage or work on your laptop, keeping the journey smooth and enjoyable.
5. Focus Flow - LoRoom: Ideal for moments when you need gentle concentration, this lofi track helps you stay productive or engrossed in your favorite book.
6. Midnight Coding - LoRoom: Maintain a steady, comfortable rhythm with this lofi track, perfect for sustained relaxation or light activity during the longer flight segment.
7. Bad Guy - Billie Eilish: A distinct shift in rhythm and mood, this song offers a brief, intriguing change of pace to re-energize slightly during the middle of your journey.
8. As It Was - Harry Styles: This popular pop track provides a familiar and slightly more upbeat interlude, serving as a momentary lift in energy during a long flight.
9. Takedown - Valorant: This intense track offers a powerful burst of energy, perhaps for when you need a strong mental jolt or a brief escape into a different soundscape.
10. Pink Venom - BLACKPINK: Finish your playlist with this dynamic and energetic track, offering a bold rhythmic push for the final stretch as you prepare for landing.

If AI API Fails:
The system displays the original top recommendations ranked by score.

---

## Design Decisions

I chose to keep the original deterministic recommender because it already provided transparent scoring and reliable ranking. Instead of replacing it, I enhanced it with AI. I noticed that the original rationale behind the rankings seemed unclear due to the jargon used and details of scores that users probably will not care for. Using RAG and Gemini AI, the program now slightly reorders ranking specifically for a plane ride and provides readable rationale.

Strengths:
- Traditional logic handles structured ranking well.
- Gemini handles sequencing, and intuitive explanations.

Trade-offs:
- Small local dataset limits recommendation diversity.
- AI output depends on prompt quality.
- Gemini mode requires internet/API access.

---

## Testing Summary

What Worked:
- Song retrieval consistently returned relevant recommendations.
- Gemini successfully reordered songs into smoother playlists.
- Fallback logic worked when AI errors occurred.

What Did Not Work Initially:
- Early prompts were too vague.
- AI occasionally attempted to mention songs not in the retrieved list.
- Parsing AI output: too unpredictable to rely on exact formatting.

Fixes:
- Added strict prompt instructions to only use retrieved songs.
- Printed AI output directly instead of attempting to parse it.
- Added try/except fallback behavior in case of API failure.

---

## Reflection
This project taught me that useful AI systems are usually hybrids of traditional projects/systems and AI models. I learned about the effectiveness in using AI to enhance original output and make it more readable. My scoring engine was effective at structured ranking, while Gemini was better at language generation, sequencing, and personalization.

I also learned that retrieval is critical. Instead of letting AI guess recommendations, grounding it with retrieved songs from my local system makes outputs more reliable and controllable.

More importantly, I learned that strong AI systems are not just model calls. They require architecture, constraints, fallback handling, and thoughtful integration. This is why it's so important to have a strong base system working before doing AI calls. Because AI calls are unpredictable and often need a lot of context, it is much better to have it tweak rather than do core logic. Overall, this was a great experience!

--

## Testing
Human evaluation: Overall, the AI's output is stable and generally works. Although it rarely keeps up with tiny formatting details such as adding a newline between each recommended song, it has consistently not deleted songs / added new songs and provided reasonable rationales for ordering. However, the AI did struggle under minimal context/instructions, which is why clear instructions are important.

--

## Reflection and Ethics




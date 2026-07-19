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

The system has three main layers (system diagram is under assets folder):

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

If AI API Fails:
The system displays the original top recommendations ranked by score.

---

## Design Decisions

I chose to keep the original deterministic recommender because it already performed the structured parts of the task well. It filtered songs, calculated weighted scores based on factors such as mood, genre, energy, danceability, and valence, and produced a consistent ranking. Because this logic is rule-based, it is transparent, reproducible, and easier to debug than asking an AI model to generate recommendations from scratch.

However, the original output was not very user-friendly. It mainly showed song rankings and numeric scores, which explained how the system made decisions technically but did not clearly explain why a user might enjoy each song. Terms such as valence, weighted similarity, and danceability may be useful during development, but most users are more interested in whether a song fits their mood and where it belongs in the listening experience.

Instead of replacing the reliable recommender with Gemini, I used AI as an enhancement layer. The deterministic system still controls which songs are eligible and retrieves the strongest matches. Only those retrieved songs are passed to Gemini, along with the user’s preferences and the plane-ride context.

Gemini then performs a task that is harder to express with fixed scoring rules: it slightly reorders the songs into a more natural listening journey. For example, it may place energetic songs near takeoff, calmer songs during the middle of the flight, and reflective or relaxing songs near the end. It also generates readable explanations describing why each song fits that position and how it relates to the user’s preferences.

This hybrid design gives each component a clear responsibility. The traditional recommender handles filtering, scoring, and reliable retrieval, while Gemini handles contextual sequencing and natural-language explanation. This makes the system more engaging without giving the AI unrestricted control over the recommendations.

There is also an important trade-off in this design. Because Gemini can reorder the retrieved songs, the final playlist may not follow the exact numerical ranking produced by the original algorithm. However, the model is constrained to the retrieved set, so it cannot freely recommend unrelated songs. This preserves much of the original system’s reliability while allowing the final output to feel more personalized and appropriate for the travel scenario.

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
Human evaluation: I've run my program many (15+) times to evaluate the AI' ourput and reliability. Overall, the AI's output is stable and generally works. Although it rarely keeps up with tiny formatting details such as adding a newline between each recommended song, it has consistently not deleted songs / added new songs and provided reasonable rationales for ordering. However, the AI did struggle under minimal context/instructions, which is why clear instructions are important.

--

## Reflection and Ethics
One limitation of this system is that it relies on a small song dataset which means that its recommendations are limited to the songs available. Also, if the dataset is biased in any way or overrepresents certain genres, the system will probably favor those genres while underrepresenting others. Another limitation is that user music preferences are simplified to fit into individual scores such as mood, energy, and danceability, but the reality is that music taste is more complex and can depend on more factors such as memories and cultural background. Finally, the Gemini playlist layer may also produce subjective outputs. Even when grounded by retrieved songs, the ordering or explanations might not always match what every user actually prefers.

One misuse of this system would be presenting these AI-influenced recommendations as objectively correct rather than taking them with a grain of salt. Music preference is personal, so recommendations should be framed as guidance rather than facts. Also, AI could possibly invent songs or delete songs. Although I reduced this risk by telling Gemini to only use songs from the given list, there is still a possibility of AI hallucination.

What surprised me most was how important prompt wording was. Small changes in instructions significantly changed whether the AI stayed obedient or not. I was also surprised that my traditional recommendation logic was more reliable than AI for ranking songs consistently. My recommendation engine produced stable results, while Gemini was better at personalization, sequencing, and intuitive explanations. This taught me that it is best to combine working software with AI rather than replacing one with the other.

Throughout my building process, I used AI for brainstorming, debugging and prompt refinement. One helpful AI suggestion was to enhance my existing recommender with Gemini API calls instead of replacing it in any way. Using this suggestion, I was able to brainstorm a good use of RAG with my original music recommender simulation. One flawed suggestion was with the mermaid.js diagram. Although I gave the AI my original mermaid.js diagram and specifically asked it to just add the Gemini API call and error handling to the tail end of it, it still overcomplicated the diagram a couple of times. It was only after a few tries that it gave me the diagram I was looking for.

In the future, I would like to expand this project by including a more comprehensive dataset of songs. I would have the AI use the comprehensive set of songs to provide more detailed rationale as to why that song was chosen, and I think a more detailed dataset would also help the AI be more accurate with its choices. I would also like to allow the user to input their own music preferences rather than choosing from one of the provided ones.

Overall, AI was most helpful when used as a collaborator for ideas and debugging, but I still needed to make final decisions, especially with system design, myself.

--

## Demo Questions for Students
1. What part of this system is already working reliably without AI?
      Expected answer: filtering, scoring, and ranking.
      Why ask it: reinforces that students should preserve useful existing logic instead of replacing everything with an LLM.

2. What does Gemini add that the original recommender could not do as well?
      Expected answer: contextual sequencing and clearer, user-friendly explanations.
      Why ask it: helps students distinguish between traditional logic and the specific value of AI.

3. Why do I give Gemini only the retrieved songs instead of asking it to recommend any songs it wants?
      Expected answer: better grounding, fewer hallucinations, more control, and stronger integration with the original project.
      Why ask it: checks whether they understand why retrieval matters.


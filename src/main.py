"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs
from rag import generate_ai_playlist

def main() -> None:
    songs = load_songs("data/songs.csv")
    #print(f'Loaded songs: {len(songs)}')

    # High-energy pop
    high_energy_pop_profile = {
        "min_valence": 0.4,
        "max_valence": 1,
        "favorite_mood": "happy",
        "mood_tolerance": ["chill", "focused"],
        "preferred_genres": ["pop", "indie pop", "k-pop"],
        "target_energy": 0.8,
        "target_danceability": 0.7
    }

    # Sad Gym Junkie (edge case)
    edge_case_profile = {
        "min_valence": 0.2,
        "max_valence": 0.5,
        "favorite_mood": "intense",
        "mood_tolerance": ["sad", "moody"],
        "preferred_genres": ["rock", "metal", "synthwave"],
        "target_energy": 0.9,
        "target_danceability": 0.65
    }

    # Chill Lofi
    chill_lofi_profile = {
        "min_valence": 0.5,
        "max_valence": 0.75,
        "favorite_mood": "chill",
        "mood_tolerance": ["relaxed", "focused"],
        "preferred_genres": ["lofi", "ambient", "jazz"],
        "target_energy": 0.35,
        "target_danceability": 0.45    
    }

    # Deep Intense Rock
    intense_rock_profile = {
        "min_valence": 0.4,
        "max_valence": 0.8,
        "favorite_mood": "intense",
        "mood_tolerance": ["moody", "energetic"],
        "preferred_genres": ["rock", "synthwave", "metal"],
        "target_energy": 0.88,
        "target_danceability": 0.7, 
        "likes_acoustic": False,  
    }

    


    #recommendations = recommend_songs(high_energy_pop_profile, songs, k=5)
    preliminary_recommendations = recommend_songs(high_energy_pop_profile, songs, k=10)
    user_profile_str = str(high_energy_pop_profile)
    recommendations = generate_ai_playlist(user_profile_str, preliminary_recommendations)

    print("\n🎧 Top Recommendations 🎧\n")
    print("=" * 50)
    '''
    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec

        print(f"\n{i}. {song['title']}")
        print(f"   Score: {score:.2f}")
    
        print("   Reasons:")
        for reason in explanation.split("; "):
            print(f"     - {reason}")

    print("\n" + "=" * 50)
    '''
    print(recommendations)


if __name__ == "__main__":
    main()

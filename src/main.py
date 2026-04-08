"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    # Supports module execution: python -m src.main
    from .recommender import load_songs, recommend_songs
except ImportError:
    # Supports direct script execution: python src/main.py
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded {len(songs)} songs.")

    # Sample user preference profiles for quick experimentation.
    user_profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.85,
            "likes_acoustic": False,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35,
            "likes_acoustic": True,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.9,
            "likes_acoustic": False,
        },
        "Rock But Calm Mood Clash": {
            "genre": "rock",
            "mood": "peaceful",
            "energy": 0.92,
            "likes_acoustic": True
        },
        "Ultra-Low Energy Party Ask": {
            "genre": "electronic",
            "mood": "energetic",
            "energy": 0.05,
            "likes_acoustic": False
        },
        "Acoustic Contradiction Profile": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35,
            "likes_acoustic": False
        }
    }

    # Loop through each profile and show top 5 recommendations
    for profile_name, user_prefs in user_profiles.items():
        print(f"\n{'='*70}")
        print(f"Profile: {profile_name}")
        print(f"Preferences: {user_prefs}")
        print(f"{'='*70}\n")

        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("Top 5 recommendations:\n")
        for rank, rec in enumerate(recommendations, start=1):
            # The recommender returns (song, score, explanation).
            song, score, explanation = rec
            reasons = [] if explanation == "No strong preference matches" else [r.strip() for r in explanation.split(",")]

            print(f"{rank}. {song['title']} by {song['artist']}")
            print(f"   Score: {score}")
            print(f"   Genre: {song['genre']}, Mood: {song['mood']}, Energy: {song['energy']}")
            if reasons:
                print(f"   Match: {', '.join(reasons)}")
            else:
                print("   Match: No strong preference matches")
            print()


if __name__ == "__main__":
    main()

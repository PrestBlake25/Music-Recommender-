# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**Find My Vibe 1.0**  

---

## 2. Intended Use  

This recommender suggests top songs from a small catalog based on a user's genre, mood, energy, and acoustic preference. It assumes users can describe their taste with a few simple settings. It is designed for classroom exploration, not real production use.

---

## 3. How the Model Works  

The model compares each song to the user's preferred genre, mood, target energy, and acoustic preference. Songs get points for matching each preference, then the list is sorted by total score. I changed the weights to make mood stronger than genre (mood +4, genre +2) and kept energy/acoustic matching plus a small energy proximity bonus to reduce ties.

---

## 4. Data  

The dataset has 18 songs in data/songs.csv. It includes multiple genres (pop, lofi, rock, electronic, jazz, classical, hip-hop, and more) and varied moods (happy, chill, intense, peaceful, energetic, etc.). I did not add or remove songs. The catalog is still small, so many real-world tastes and subgenres are missing.

---

## 5. Strengths  

The system works well when user preferences align with well-represented styles, such as Chill Lofi and High-Energy Pop. It reliably prioritizes songs that match the target mood and energy. Results matched my intuition in profiles with clear, non-conflicting preferences.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

This recommender uses mostly exact matches and limited partial credit. Users with rare moods/genres can be under-served, and near-matches may rank too low. A small dataset also increases bias toward the most represented styles.
---

## 7. Evaluation  

I tested six profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, Rock But Calm Mood Clash, Ultra-Low Energy Party Ask, and Acoustic Contradiction Profile. I checked whether top 5 songs matched genre, mood, energy, and acoustic preferences. I also compared rankings before and after changing weights (genre +4 to +2, mood +3 to +4). Small weight changes shifted rankings quickly, and unusual preference combinations were hardest to satisfy.

---

## 8. Future Work  

Add more features like tempo ranges, valence, and artist variety controls. Improve explanations by showing a short score breakdown for each recommendation, providing partial credit. Add diversity rules so top results are not too similar. Support more complex tastes, such as mixed moods or multi-user/group profiles.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned that engineering systems with AI can be difficult, having to read the varbose responses that Copilot or Claude gives you to probably give code that you may or may not understand, but it helps that you skim through it and see the code to find some sense in it. The AI tools that helped me were Copilot, and it helped me to see how recommendations are tracked by some sort of scoring algorithm.
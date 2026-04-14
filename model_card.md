# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 
One weakness I discovered during my experiments is that my system favors labels over actual music. Since genre and mood account for about 70% of a song's score, and both of these are just labels of a song rather than the song's actual music, my system favors easily classifiable songs. For example, songs that can easily be classified as "happy" mood and "pop" genre are more likely to appear correctly versus songs that fit under multiple moods and genres are less likely to be recommended. My system also struggles to output a diverse set of song recommendations, and does not allow room for the user to listen to new kinds of songs.


---

## 7. Evaluation  
I tested my recommender on four different user profiles: happy/pop, lofi/chill, edge case (prefer high energy but sad genre), and heavy rock. For each of these cases, I looked at the songs recommended and their corresponding genres, moods, and energy levels, and for all cases, the recommendations seemed accurate and reasonable. None of the recommendations surprised me too much.
Since many of the songs in my dataset are easily classifiable, the recommendations did not really change too much even after I eliminated the genre feature from scoring. However, I did notice that once I removed the genre feature, some songs that sort of sound like a particular genre, such as Takedown sounding like pop but being classified under rock, showed up under happy/pop. Removing genre gave more preference to actual musical content rather than labels, which can be good or bad depending on perspective.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

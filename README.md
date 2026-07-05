# 🤖 Smart AI Recommendation System
### Content-Based Recommendation Engine using TF-IDF & Cosine Similarity

## 📊 Description

Smart AI Recommendation System is a content-based recommendation engine developed as the third project of my Artificial Intelligence Internship at DecodeLabs. It uses TF-IDF Vectorization and Cosine Similarity to recommend relevant content based on a user's interests. The project includes both a command-line application and a Tkinter-based desktop GUI.

## ✨ Features

- **TF-IDF + Cosine Similarity** — matches user interests against a tagged dataset
- **Command-line version** (`main.py`) — quick terminal-based recommendations
- **GUI version** (`gui.py`) — Tkinter desktop app with:
  - Name & interest input fields
  - Match percentage progress bar
  - Save results to `history.txt`
  - Clear/reset button

## 📁 Project Structure

```
ai-recommendation-system/
├── main.py              # CLI version
├── gui.py                # Tkinter GUI version
├── recommendation.py      # Core recommendation engine (TF-IDF + cosine similarity)
├── dataset.csv            # Titles, categories, and tags used for matching
├── requirements.txt
└── README.md
```

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- Tkinter
- CSV
## 🛠️ Requirements

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

**Command-line version:**
```bash
python3 main.py
```

**GUI version:**
```bash
python3 gui.py
```

## 💬 Example

```
Enter Your Name : Ali
Your Interests  : python ai machine learning

Hello Ali

Top AI Recommendations
--------------------------------------------
Title : Machine Learning Basics
Category : AI
Match : 87.32 %
--------------------------------------------
```

## 🧠 How It Works

1. `recommendation.py` loads `dataset.csv` and converts the `Tags` column into TF-IDF vectors
2. The user's interest string is vectorized the same way
3. Cosine similarity is calculated between the user's input and every item's tags
4. Results are sorted by similarity score and the top matches (score > 0) are returned

## 📚 Learning Outcomes

- Content-Based Recommendation Systems
- Natural Language Processing (TF-IDF)
- Cosine Similarity
- GUI Development with Tkinter
- File Handling
- Python OOP

## 🚀 Future Improvements

- User Login System
- Recommendation History Database
- Collaborative Filtering
- Web Application using Flask
- Image-based Recommendations


## 👩‍💻 Author

**Nahah Butt**

BS Artificial Intelligence

Python Developer Intern @ DecodeLabs
## 📄 License

This project was developed for educational purposes as the **third project** of my Artificial Intelligence Internship at DecodeLabs.

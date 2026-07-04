# 🤖 Smart AI Recommendation System

A content-based recommendation system built with **TF-IDF vectorization** and **cosine similarity**, available both as a command-line tool and a desktop GUI app (Tkinter).

## 📊 Description

Enter your interests (e.g. "python ai machine learning") and the system recommends the top matching titles from a dataset, ranked by similarity score.

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

## 👤 Author

Nahah Butt | BS Artificial Intelligence

## 📄 License

This project is for educational purposes--- Third project of Artificial Intelligence Internship.

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class RecommendationEngine:

    def __init__(self, dataset):
        self.data = pd.read_csv(dataset)
        self.vectorizer = TfidfVectorizer()
        self.matrix = self.vectorizer.fit_transform(self.data["Tags"])

    def cosine_sim(self, user_input, tags):
        user_vector = self.vectorizer.transform([user_input])
        scores = cosine_similarity(
            user_vector,
            self.vectorizer.transform(tags)
        )
        return scores.flatten()

    def recommend(self, interests, top=5):
        interests = interests.lower()

        self.data["Score"] = self.cosine_sim(
            interests,
            self.data["Tags"]
        )

        result = self.data.sort_values(
            by="Score",
            ascending=False
        )

        # Sirf matching results
        result = result[result["Score"] > 0]

        return result.head(top)
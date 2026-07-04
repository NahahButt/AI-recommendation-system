from recommendation import RecommendationEngine

print("=" * 60)
print("      SMART AI RECOMMENDATION SYSTEM")
print("=" * 60)

name = input("Enter Your Name : ")

print("\nEnter Interests")
print("Example:")
print("python ai machine learning")

interest = input("\nYour Interests : ")

engine = RecommendationEngine("dataset.csv")

result = engine.recommend(interest)

print("\nHello", name)
print("\nTop AI Recommendations\n")

for i, row in result.iterrows():

    print("--------------------------------------------")

    print("Title :", row["Title"])

    print("Category :", row["Category"])

    print("Match :", round(row["Score"] * 100, 2), "%")

print("--------------------------------------------")
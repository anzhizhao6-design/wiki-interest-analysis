import pandas as pd

df = pd.read_csv("wiki_project/wiki_results.csv")

interest_keywords = {
    "AI / Technology": ["artificial intelligence", "AI", "machine learning", "data", "computer", "technology"],
    "Music": ["music", "singer", "songwriter", "album", "pop", "rock"],
    "Business": ["business", "company", "entrepreneur", "market", "finance"],
    "Science": ["research", "scientist", "physics", "biology", "chemistry"],
    "Sports": ["sport", "player", "team", "coach", "competition"]
}

text = " ".join(df["summary"].astype(str)).lower()
print("=== Wikipedia Data Report ===")
print("Total records:", len(df))

print("\nColumns:")
print(df.columns.tolist())

print("\nPreview:")
print(df[["keyword", "title"]])

print("\nLongest summary:")
df["summary_length"] = df["summary"].astype(str).apply(len)
longest = df.sort_values("summary_length", ascending=False).iloc[0]

print("Keyword:", longest["keyword"])
print("Title:", longest["title"])
print("Summary length:", longest["summary_length"])

print("\n=== Interest Direction Analysis ===")
scores = {}
for category,keywords in interest_keywords.items():
    score = 0 
    for w in keywords:
        if w.lower() in text:
            score += text.count(w.lower())
    scores[category] = score
for category, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    print(category, ":", score)
top_category = max(scores, key=scores.get)
print("\nMost likely interest direction:", top_category)
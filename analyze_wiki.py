import pandas as pd

CSV_FILE = "data/processed/wiki_results.csv"

interest_keywords = {
    "AI / Technology": ["artificial intelligence", "ai", "machine learning", "data", "computer", "technology"],
    "Music": ["music", "singer", "songwriter", "album", "pop", "rock"],
    "Business": ["business", "company", "entrepreneur", "market", "finance"],
    "Science": ["research", "scientist", "physics", "biology", "chemistry"],
    "Sports": ["sport", "player", "team", "coach", "competition"]
}

def analyze_records(records):
    df = pd.DataFrame(records)
    text = " ".join(df["summary"].astype(str)).lower()

    scores = {}
    for category, keywords in interest_keywords.items():
        scores[category] = sum(text.count(w.lower()) for w in keywords)

    df["summary_length"] = df["summary"].astype(str).apply(len)
    longest = df.sort_values("summary_length", ascending=False).iloc[0]

    return {
        "total_records": len(df),
        "columns": df.columns.tolist(),
        "preview": df[["keyword", "title"]],
        "longest_keyword": longest["keyword"],
        "longest_title": longest["title"],
        "longest_summary_length": longest["summary_length"],
        "scores": scores,
        "top_category": max(scores, key=scores.get)
    }


def analyze_data():
    df = pd.read_csv(CSV_FILE)
    return analyze_records(df.to_dict("records"))


if __name__ == "__main__":
    report = analyze_data()

    print("=== Wikipedia Data Report ===")
    print("Total records:", report["total_records"])

    print("\nColumns:")
    print(report["columns"])

    print("\nPreview:")
    print(report["preview"])

    print("\nLongest summary:")
    print("Keyword:", report["longest_keyword"])
    print("Title:", report["longest_title"])
    print("Summary length:", report["longest_summary_length"])

    print("\n=== Interest Direction Analysis ===")
    for category, score in sorted(report["scores"].items(), key=lambda x: x[1], reverse=True):
        print(category, ":", score)

    print("\nMost likely interest direction:", report["top_category"])
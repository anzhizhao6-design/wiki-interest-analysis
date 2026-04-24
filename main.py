from wiki_search import search_wiki, save_to_csv
from analyze_wiki import analyze_data

print("Step 1: Collecting data...")

names = input("Enter names, separated by comma: ").split(",")
results = search_wiki(names)
save_to_csv(results)

print("\nStep 2: Analyzing data...")

report = analyze_data()

print("=== Wikipedia Data Report ===")
print("Total records:", report["total_records"])

print("\nPreview:")
print(report["preview"])

print("\n=== Interest Direction Analysis ===")
for category, score in sorted(report["scores"].items(), key=lambda x: x[1], reverse=True):
    print(category, ":", score)

print("\nMost likely interest direction:", report["top_category"])
import os

print("Step 1: Collecting data...")
os.system("python3 wiki_project/wiki_search.py")

print("\nStep 2: Analyzing data...")
os.system("python3 wiki_project/analyze_wiki.py")
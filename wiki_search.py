import requests
from bs4 import BeautifulSoup
import csv
import urllib.parse
import time
import os

names = input("Enter names, separated by comma: ").split(",")

results = []

for name in names:
    keyword = name.strip()
    encoded_keyword = urllib.parse.quote(keyword)
    url = f"https://en.wikipedia.org/wiki/Special:Search?search={encoded_keyword}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("title")
    title_text = title.get_text() if title else "No title found"

    paragraphs = soup.find_all("p")
    summary = "N/A"

    for p in paragraphs:
        text = p.get_text().strip()
        if len(text) > 80:
            summary = text
            break

    results.append({
        "keyword": keyword,
        "title": title_text,
        "summary": summary,
        "url": response.url
    })

    print("Collected:", keyword)
    time.sleep(1)

file_exists = os.path.isfile("wiki_project/wiki_results.csv")

with open("wiki_project/wiki_results.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["keyword", "title", "summary", "url"]
    )

    if not file_exists:
        writer.writeheader()

    writer.writerows(results)

print("Done! Results appended to wiki_results.csv")
import requests
from bs4 import BeautifulSoup
import csv
import urllib.parse
import os
import time

CSV_FILE = "data/processed/wiki_results.csv"

def search_wiki(names):
    results = []

    for name in names:
        keyword = name.strip()
        if not keyword:
            continue

        encoded_keyword = urllib.parse.quote(keyword)
        url = f"https://en.wikipedia.org/wiki/Special:Search?search={encoded_keyword}"
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(url, headers=headers, timeout=10)
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

    return results


def save_to_csv(results):
    os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["keyword", "title", "summary", "url"]
        )

        if not file_exists:
            writer.writeheader()

        writer.writerows(results)

    print("Done! Results appended to wiki_results.csv")


if __name__ == "__main__":
    names = input("Enter names, separated by comma: ").split(",")
    results = search_wiki(names)
    save_to_csv(results)
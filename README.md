# Wikipedia Interest Analysis Tool

## Project Description
This project implements a simple Python-based data pipeline that collects, stores, and analyzes Wikipedia data to infer potential user interests.

The system takes user input, retrieves relevant Wikipedia pages, extracts key information, and performs keyword-based analysis to identify interest categories.


## How It Works

### Step 1: Data Collection
- Accepts multiple keywords from user input
- Sends HTTP requests to Wikipedia search pages
- Parses HTML content using BeautifulSoup
- Extracts page title, summary, and URL

### Step 2: Data Storage
- Stores structured results into a CSV file (`wiki_results.csv`)
- Appends new records if the file already exists

### Step 3: Data Analysis
- Loads data using pandas
- Processes summaries and counts keyword occurrences
- Classifies interests into categories:
  - AI / Technology
  - Music
  - Business
  - Sports
  - Science


## How to Run

```bash
python3 main.py
```

## Skills Demonstrated

- Python scripting for automation
- Web scraping using `requests` and `BeautifulSoup`
- Data processing and storage (CSV, pandas)
- Working in Linux / WSL environment
- Designing a simple data pipeline (collection → storage → analysis)


## Possible Improvements

- Implement real-time monitoring (e.g. periodic scraping)
- Build a simple UI using Streamlit
- Apply NLP techniques for more accurate analysis
- Replace scraping with official APIs
- Store data in a database instead of CSV
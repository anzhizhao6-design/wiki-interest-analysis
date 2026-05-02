# Wikipedia Interest Analysis Tool

## Project Description
This project implements a simple Python-based data pipeline that collects, stores, and analyzes Wikipedia data to infer potential user interests.

The system takes user input, retrieves relevant Wikipedia pages, extracts key information, and performs keyword-based analysis to identify interest categories.

This project demonstrates a complete data pipeline from data collection to analysis, with both CLI and web-based user interfaces.

## How It Works

### Step 1: Data Collection
- Accepts multiple keywords from user input
- Sends HTTP requests to Wikipedia search pages
- Parses HTML content using BeautifulSoup
- Extracts page title, summary, and URL

### Step 2: Data Storage
- Stores structured results into `data/processed/wiki_results.csv`
- Appends new records if the file already exists

> **Note:** The CSV data file is not included in this repository and is listed in `.gitignore`.
> Run the program to regenerate it locally.

### Step 3: Data Analysis
- Loads data using pandas
- Processes summaries and counts keyword occurrences
- Classifies interests into categories:
  - AI / Technology
  - Music
  - Business
  - Sports
  - Science

## Project Structure

```
wiki-interest-analysis/
├── data/
│   ├── raw/          # Placeholder for raw data
│   └── processed/    # Generated CSV output (git-ignored)
├── app.py            # Streamlit web UI
├── analyze_wiki.py   # Interest analysis logic
├── wiki_search.py    # Wikipedia scraping and CSV storage
├── main.py           # CLI entry point
└── requirements.txt
```

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run with CLI

```bash
python main.py
```

Enter one or more comma-separated keywords when prompted (e.g. `Python, jazz, tennis`). Results are saved to `data/processed/wiki_results.csv` and an interest analysis is printed.

### Run with Web UI

```bash
streamlit run app.py
```

Open the URL shown in your terminal. Enter keywords in the text box and click **Run Analysis** to collect data and view results interactively.

## Skills Demonstrated

- Python scripting for automation
- Web scraping using `requests` and `BeautifulSoup`
- Data processing and storage (CSV, pandas)
- Designing a simple data pipeline (collection → storage → analysis)
- Streamlit for interactive data applications

## Possible Improvements

- Implement real-time monitoring (e.g. periodic scraping)
- Apply NLP techniques for more accurate analysis
- Replace scraping with official Wikipedia API
- Store data in a database instead of CSV
- Improve the UI with better layout and visualization

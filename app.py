import os
import streamlit as st
import pandas as pd
from wiki_search import search_wiki, save_to_csv
from analyze_wiki import analyze_data

CSV_FILE = "data/processed/wiki_results.csv"

st.subheader("Recent Searches")
if os.path.isfile(CSV_FILE):
    df = pd.read_csv(CSV_FILE)
    st.dataframe(df.tail(10))
else:
    st.info("No data yet. Run an analysis below to get started.")

st.title("Wikipedia Interest Analysis Tool")

user_input = st.text_input("Enter keywords, separated by comma:")

if st.button("Run Analysis"):
    if not user_input.strip():
        st.warning("Please enter at least one keyword.")
    else:
        names = user_input.split(",")

        with st.spinner("Collecting Wikipedia data..."):
            results = search_wiki(names)
            save_to_csv(results)

        st.success("Data collection completed!")

        st.subheader("Collected Results")
        st.dataframe(pd.DataFrame(results))

        with st.spinner("Analyzing interests..."):
            report = analyze_data()

        st.subheader("Interest Direction Scores")
        scores_df = pd.DataFrame(
            list(report["scores"].items()),
            columns=["Category", "Score"]
        )

        st.dataframe(scores_df)
        st.bar_chart(scores_df.set_index("Category"))

        st.subheader("Most Likely Interest Direction")
        st.write(report["top_category"])
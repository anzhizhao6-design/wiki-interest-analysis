import streamlit as st
import pandas as pd
from wiki_search import search_wiki
from analyze_wiki import analyze_records

if "results" not in st.session_state:
    st.session_state.results = []

st.title("Wikipedia Interest Analysis Tool")

user_input = st.text_input("Enter keywords, separated by comma:")

col1, col2 = st.columns([1, 1])
with col1:
    run = st.button("Run Analysis")
with col2:
    if st.button("Clear Session"):
        st.session_state.results = []
        st.rerun()

if run:
    if not user_input.strip():
        st.warning("Please enter at least one keyword.")
    else:
        with st.spinner("Collecting Wikipedia data..."):
            new_results = search_wiki(user_input.split(","))
            st.session_state.results.extend(new_results)
        st.success(f"Added {len(new_results)} result(s) to your session.")

if st.session_state.results:
    results_df = pd.DataFrame(st.session_state.results)

    st.subheader("This Session's Results")
    st.dataframe(results_df[["keyword", "title", "url"]])

    report = analyze_records(st.session_state.results)

    st.subheader("Interest Direction Scores")
    scores_df = pd.DataFrame(
        list(report["scores"].items()),
        columns=["Category", "Score"]
    ).sort_values("Score", ascending=False)
    st.dataframe(scores_df)
    st.bar_chart(scores_df.set_index("Category"))

    st.subheader("Most Likely Interest Direction")
    st.write(report["top_category"])

    st.download_button(
        label="Download session results as CSV",
        data=results_df.to_csv(index=False).encode("utf-8"),
        file_name="wiki_results.csv",
        mime="text/csv",
    )
else:
    st.info("No data yet. Enter keywords above and click Run Analysis.")

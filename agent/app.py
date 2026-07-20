import streamlit as st
from agent import answer_question

st.set_page_config(
    page_title="TechSolve AI Data Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 TechSolve AI Data Analysis Agent")

st.write(
    "Ask natural-language questions about the TechSolve customer support dataset."
)

question = st.text_input(
    "Ask a question:",
    placeholder="Example: How many total rows are in this dataset?"
)

if st.button("Analyse"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:
        with st.spinner("Analysing the dataset..."):

            try:
                answer = answer_question(question)

                st.subheader("Analysis Result")
                st.write(answer)

            except Exception as e:
                st.error(f"An error occurred: {e}")

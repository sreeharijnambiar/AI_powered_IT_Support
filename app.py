import streamlit as st
from retrieval import process_query

st.set_page_config(
    page_title="AI IT Support Assistant"
)

st.title("🛠️ AI IT Support Assistant")

query = st.chat_input(
    "Describe your IT issue..."
)

if query:

    st.chat_message("user").write(query)

    with st.spinner("Analyzing historical tickets..."):
        response = process_query(query)

    st.chat_message("assistant").write(response)
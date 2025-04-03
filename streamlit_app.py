import streamlit as st
from chat_sql import ask_db

st.set_page_config(page_title="Chat with Azure SQL", page_icon="🧠")
st.title("💬 Chat with Azure SQL Database")

question = st.text_input("Ask a question about your data:", placeholder="e.g., How many rows are in the Sales table?")

if question:
    with st.spinner("Thinking..."):
        try:
            result = ask_db(question)
            st.success("Done!")
            st.code(result, language="sql")
        except Exception as e:
            st.error(f"❌ Error: {e}")


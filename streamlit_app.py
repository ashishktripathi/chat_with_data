import streamlit as st
from chat_sql import ask_db

st.set_page_config(page_title="Chat with Azure SQL Database", page_icon="💬")
st.title("💬 Chat with Azure SQL Database")

# Initialize session state to store conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box at the bottom
if prompt := st.chat_input("Ask a question about your data:"):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Run the query + display result
    try:
        response = ask_db(prompt)
        formatted = str(response)

        st.chat_message("assistant").markdown(f"```python\n{formatted}\n```")
        st.session_state.messages.append({"role": "assistant", "content": f"```python\n{formatted}\n```"})
    except Exception as e:
        st.chat_message("assistant").markdown("Error: " + str(e))
        st.session_state.messages.append({"role": "assistant", "content": "Error: " + str(e)})

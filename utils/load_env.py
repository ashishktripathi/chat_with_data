import os
from dotenv import load_dotenv

def load_environment():
    # If running locally, load from .env
    if os.getenv("STREAMLIT_CLOUD") != "true":
        from pathlib import Path
        env_path = Path(__file__).parent.parent / '.env'
        load_dotenv(dotenv_path=env_path)
    else:
        # In Streamlit Cloud, read from st.secrets
        import streamlit as st
        for key, value in st.secrets.items():
            os.environ[key] = value

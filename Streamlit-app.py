import  streamlit as st
from helper import get_matches

st.set_page_config(page_title = "JINA AUDIO SEARCH")

st.title("Beat Recommender")

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    # to read files as bytes:
        bytes_data = uploaded_file.getvalue()
        
        matches = get_matches(bytes_data)
        
        if not matches:
            st.write("No matches found :(")
        
        for match in matches:
            st.audio(f"../{match['uri']}")
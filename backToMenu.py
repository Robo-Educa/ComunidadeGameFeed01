import streamlit as st

def back():    
    # Menu    
    if st.button("👤Jogadores", use_container_width=True):
        st.switch_page("app.py")
    
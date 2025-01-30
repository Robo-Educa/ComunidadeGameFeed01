import streamlit as st

def text_center(msg):
    st.markdown(
        f"""
        <h1 style='text-align: center;'>{msg}</h1>
        """,
        unsafe_allow_html=True,
    )
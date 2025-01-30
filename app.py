# Importa Streamlit
import streamlit as st
from menu import render_menu

st.set_page_config(page_title="Comunidade Game - Feed", page_icon=":material/support_agent:", layout="centered", initial_sidebar_state="collapsed")
st.sidebar.title("Comunidade Game")

# Menu
render_menu()

# Imagem
st.image(image="./static/logo.jpg", use_column_width=True)

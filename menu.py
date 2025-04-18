import streamlit as st
from layout import text_center

def main_menu():
    # Header
    text_center("Comunidade Game")

    # Menu
    jogadores_col, mestres_col, poderes_col = st.columns(3)

    if jogadores_col.button("⭐ Jogadores", use_container_width=True):
        st.switch_page("pages/Jogadores.py")

    if mestres_col.button("🧙 Mestres", use_container_width=True):
        st.switch_page("pages/Mestres.py")
        
    if poderes_col.button("✨ Habilidades", use_container_width=True):
        st.switch_page("pages/Poderes.py")    

    comunidades_col, parceiros_col = st.columns(2)

    if comunidades_col.button("📍 Comunidades", use_container_width=True):
        st.switch_page("pages/Comunidades.py")

    if parceiros_col.button("🔗 Parceiros", use_container_width=True):
        st.switch_page("pages/Parceiros.py")

def back_to_main_menu():  
    if st.button("↩️", use_container_width=True):
        st.switch_page("app.py")

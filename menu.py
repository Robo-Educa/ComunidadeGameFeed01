import streamlit as st
from layout import text_center

def render_menu():
    # Header
    text_center("Comunidade Game")

    # Menu
    jogadores_col, mestres_col, parceiros_col = st.columns(3)

    if jogadores_col.button("👤Jogadores", use_container_width=True):
        st.switch_page("pages/Jogadores.py")
    if mestres_col.button("🎓Mestres", use_container_width=True):
        st.switch_page("pages/Mestres.py")
    if parceiros_col.button("🤝 Parceiros", use_container_width=True):
        st.switch_page("pages/Parceiros.py")    

def back_to_menu():  
    if st.button("↩️", use_container_width=True):
        st.switch_page("app.py")


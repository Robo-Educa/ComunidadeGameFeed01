import streamlit as st
import menu as menu
import service.playerService as playerService
from layout import text_center

st.set_page_config(page_title="Jogadores - Comunidade Game", page_icon=":material/support_agent:", layout="centered", initial_sidebar_state="collapsed")

text_center("👤Jogadores")
menu.back_to_main_menu()

tab1, tab2 = st.tabs(['💠 Todos','💠 Individual'])   
with tab1:    
    df = playerService.mount_table()
    
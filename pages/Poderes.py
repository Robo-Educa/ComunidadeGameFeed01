import streamlit as st
import menu as menu
import service.poderesService as poderesService
from layout import text_center

st.set_page_config(page_title="Habilidades - Comunidade Game", page_icon=":material/support_agent:", layout="centered", initial_sidebar_state="collapsed")

# . Monta tabela com caixa de seleção
def dataframe_with_selections(df):
    df_with_selections = df.copy()
    df_with_selections.insert(0, "Select", False)

    # Get dataframe row-selections from user with st.data_editor
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        disabled=df.columns,
    )

    # Filter the dataframe using the temporary column, then drop the column
    selected_rows = edited_df[edited_df.Select]
    return selected_rows.drop('Select', axis=1)    

# . Exibe a tabela
def mount_table():        
    selection = dataframe_with_selections(st.session_state.df_docs)     

# =========
# main
# =========

# Inicializar dataframe
st.session_state.df_docs = poderesService.get_docs()

text_center("✨ Habilidades")
menu.back_to_main_menu()

tab1, tab2 = st.tabs(['💠 Todos','💠 Individual'])   
with tab1:    
    mount_table()

import streamlit as st
import menu as menu
import service.playerService as playerService
from layout import text_center
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(page_title="Jogadores - Comunidade Game", page_icon=":material/support_agent:", layout="centered", initial_sidebar_state="collapsed")

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

def sobrepor_imagens(background_path, avatar_path, nome_jogador):
    """Sobrepõe um avatar sobre um background."""

    background = Image.open(background_path).convert("RGBA")
    avatar = Image.open(avatar_path).convert("RGBA")

    # Redimensionar o avatar, se necessário
    avatar = avatar.resize((300, 300)) # Ajuste o tamanho conforme necessário

    # Calcula a posição para centralizar o avatar
    posicao = ((background.width - avatar.width) // 2,
                (background.height - avatar.height) // 2)

    # Sobrepõe o avatar sobre o background
    background.paste(avatar, posicao, avatar)

    # Adicionar o nome do jogador acima do avatar
    draw = ImageDraw.Draw(background)
    fonte = fonte = ImageFont.truetype("fonteGamer.ttf", 20) 
    texto_posicao = (background.width // 2, posicao[1] - 20)  # Ajuste o nome do jogador acima do avatar
    draw.text(texto_posicao, nome_jogador, font=fonte, fill=(255, 255, 255), anchor="mm")  # Texto branco e centralizado

    return background


# =========
# main
# =========

# Inicializar dataframe
st.session_state.df_docs = playerService.get_docs()

text_center("⭐ Jogadores")

tab1, tab2 = st.tabs(['💠 Individual','💠 Listagem'])   

with tab1:    
    background_path = "./static/background.jpg" # substitua pelo caminho da sua imagem de background
    avatar_path = "./static/avatar.png" # substitua pelo caminho da sua imagem de avatar com fundo transparente

    try:
        resultado = sobrepor_imagens(background_path, avatar_path,"Carlos Trenell")
        st.image(resultado, use_container_width=True)
    except FileNotFoundError:
        st.error("Arquivos de imagem não encontrados.")

with tab2:
    mount_table()

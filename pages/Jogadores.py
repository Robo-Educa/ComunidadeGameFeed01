import streamlit as st
import menu as menu
import service.playerService as playerService
from layout import text_center
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(page_title="Jogadores - Comunidade Game", page_icon=":material/support_agent:", layout="centered", initial_sidebar_state="collapsed")

background_path = "./static/background2.jpg" # substitua pelo caminho da sua imagem de background
avatar_path = "./static/avatar.png" # substitua pelo caminho da sua imagem de avatar com fundo transparente

def buscar_jogador(indice):
    playerService.get_docs()


def montar_imagem_jogador(background_path, avatar_path, nome_jogador, pontos, ranking):
    """Sobrepõe um avatar sobre um background."""

    background = Image.open(background_path).convert("RGBA")
    avatar = Image.open(avatar_path).convert("RGBA")

    # Redimensionar o avatar, se necessário
    avatar = avatar.resize((280, 280)) # Ajuste o tamanho conforme necessário

    # Calcula a posição para centralizar o avatar
    posicao = ((background.width - avatar.width) // 2,
                (background.height - avatar.height) // 2)
    
    # Sobrepõe o avatar sobre o background
    background.paste(avatar, posicao, avatar)
    
    # Adiciona nome do Jogador, ranking e Pontuação
    draw = ImageDraw.Draw(background)
    fonte = fonte = ImageFont.truetype("arial.ttf", 20) 

    nome_posicao = (background.width // 2, posicao[1] - 15) 
    pontos_posicao = (background.width // 2, posicao[1] + 280 + 15)  

    draw.text(nome_posicao, nome_jogador, font=fonte, fill=(255, 255, 255), anchor="mm")  # Texto branco e centralizado
    draw.text(pontos_posicao, f"{ranking}º Lugar - {pontos} pts", font=fonte, fill=(255, 255, 255), anchor="mm")  # Texto branco e centralizado

    return background

def avancar():
    return

def voltar():
    return

# =========
# main
# =========

# Inicializar dataframe
st.session_state.df_docs = playerService.get_docs()

text_center("⭐ Jogadores")

tab1, tab2 = st.tabs(['💠 Individual','💠 Todos'])   

with tab1:    
    next_col, back_col=  st.columns(2)

    if next_col.button("Anterior", use_container_width=True):
        voltar()

    if back_col.button("Próximo", use_container_width=True):
        avancar()

    try:
        resultado = montar_imagem_jogador(background_path, avatar_path, "Carlos Trenell", "500", "1")
        st.image(resultado, use_container_width=True)
    except FileNotFoundError:
        st.error("Arquivos de imagem não encontrados.")

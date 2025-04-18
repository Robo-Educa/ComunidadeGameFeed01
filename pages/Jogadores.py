import streamlit as st
import menu as menu
import service.playerService as playerService
from layout import text_center
from PIL import Image, ImageDraw, ImageFont
import requests
import time
from io import BytesIO

st.set_page_config(page_title="Jogadores - Comunidade Game", page_icon=":material/support_agent:", layout="wide", initial_sidebar_state="collapsed")

def exibir_imagem_jogador(avatar_url, nome_jogador, placeholder):
    """Sobrepõe um avatar sobre um background, com barra de progresso enquanto carrega."""
    
    # Cria a barra de progresso
    progress_bar = st.progress(0, text="Carregando avatar do jogador...")

    # Etapa 1: Carregar background
    time.sleep(0.2)
    background_path = "./static/background2.jpg" 
    background = Image.open(background_path).convert("RGBA")
    progress_bar.progress(20, text="Carregando background...")

    # Etapa 2: Baixar imagem
    response_avatar_url = requests.get(avatar_url)
    time.sleep(0.2)
    progress_bar.progress(50, text="Carregando avatar...")

    # Etapa 3: Abrir e preparar avatar
    avatar = Image.open(BytesIO(response_avatar_url.content)).convert("RGBA")
    avatar = avatar.resize((280, 280))
    progress_bar.progress(70, text="Processando imagem...")

    # Etapa 4: Montar imagem final
    posicao = ((background.width - avatar.width) // 2,
               (background.height - avatar.height) // 2)
    background.paste(avatar, posicao, avatar)

    draw = ImageDraw.Draw(background)
    fonte = ImageFont.truetype("arial.ttf", 20)
    nome_posicao = (background.width // 2, posicao[1] - 15)
    draw.text(nome_posicao, f"{nome_jogador}", font=fonte, fill=(255, 255, 255), anchor="mm")

    progress_bar.progress(100, text="Imagem pronta!")

    time.sleep(0.2)  # Dá tempo para o usuário ver o 100%
    progress_bar.empty()  # Limpa a barra

    # Exibe imagem final
    placeholder.empty()
    placeholder.image(background, use_container_width=True) 

text_center("⭐ Jogadores")
menu.back_to_main_menu()

with st.spinner("Carregando Jogadores"):
    
    jogadores = playerService.get_docs()    # Obtem listagem de todos os jogadores    

    col1, col2 = st.columns(2)

    with col1:
        if jogadores.empty == False:
            selecao  = st.radio("Selecione o Jogador desejado:", jogadores["Nick"])

    with col2:
        if jogadores.empty == False:
            placeholder = st.empty()
            jogador_url_avatar = jogadores[jogadores['Nick'] == selecao]['Avatar'].values[0]
            exibir_imagem_jogador(jogador_url_avatar, selecao, placeholder)


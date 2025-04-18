import streamlit as st
import menu as menu
import service.playerService as playerService
import service.playerAtividadesService as playerAtividadesService 
from layout import text_center
from PIL import Image, ImageDraw, ImageFont
import requests
import time
from io import BytesIO

st.set_page_config(page_title="Jogadores - Comunidade Game", page_icon=":material/support_agent:", layout="wide", initial_sidebar_state="collapsed")

def exibir_imagem_jogador(avatar_url, nome_jogador, pontos, placeholder):
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
    pontos_posicao = (background.width // 2, posicao[1] + 280 + 15)
    draw.text(nome_posicao, nome_jogador, font=fonte, fill=(255, 255, 255), anchor="mm")
    draw.text(pontos_posicao, f"{pontos} pts", font=fonte, fill=(255, 255, 255), anchor="mm")

    progress_bar.progress(100, text="Imagem pronta!")

    time.sleep(0.2)  # Dá tempo para o usuário ver o 100%
    progress_bar.empty()  # Limpa a barra

    # Exibe imagem final
    placeholder.empty()
    placeholder.image(background, use_container_width=True) 

text_center("⭐ Jogadores")
menu.back_to_main_menu()

with st.spinner("Carregando Ranking"):
    # Obtem Ranking de Jogadores - Total de pontuação individual
    ranking = playerAtividadesService.get_ranking()

col1, col2 = st.columns(2)

with col1:
    jogadores = ranking['Jogador'].tolist()
    selecao = st.radio("Selecione o Jogador desejado:", jogadores)

with col2:  
    placeholder = st.empty() # limpa área para exibição da imagem
    
    # Obtém os dados completos do jogador a partir do service
    jogador = playerService.get_doc("nick_name", selecao)
    jogador_info = jogador[0].to_dict()
    jogador_url_avatar = jogador_info.get("avatar_url", "")    
        
    # 2. pontos do jogador no dataframe ranking
    jogador_pontos = ranking[ranking['Jogador'] == selecao]['Pontos'].values[0]

    # Exibir imagem composta
    exibir_imagem_jogador(jogador_url_avatar, selecao, jogador_pontos, placeholder)

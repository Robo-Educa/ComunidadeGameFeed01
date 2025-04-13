import streamlit as st
import menu as menu
import service.playerService as playerService
import service.playerAtividadesService as playerAtividadesService 
from layout import text_center
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(page_title="Jogadores - Comunidade Game", page_icon=":material/support_agent:", layout="centered", initial_sidebar_state="collapsed")

background_path = "./static/background2.jpg" # substitua pelo caminho da sua imagem de background
avatar_path = "./static/avatar.png" # substitua pelo caminho da sua imagem de avatar com fundo transparente

def montar_imagem_jogador(background_path, avatar_path, nome_jogador, pontos, ranking, placeholder):
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

    # Exibe a imagem
    placeholder.empty() #Limpa o espaço do placeholder
    #placeholder.image(background, use_container_width=True) 
    placeholder.write(st.session_state.indice)

def mover(value, placeholder): 
    indice = int(st.session_state.indice) 
    indice =  indice + int(value)  
    # st.session_state.indice = indice
    placeholder.write(indice)
    # jogador_nick_name = ranking["Nick Name"][indice]
    # jogador_pontos = ranking["Total de Pontos"][indice]
    # montar_imagem_jogador(background_path, avatar_path, jogador_nick_name, jogador_pontos, st.session_state.indice, placeholder)

# =========
# main
# =========

# Inicializar dataframe
if not 'indice' in st.session_state:
    st.session_state.indice = 1

text_center("⭐ Jogadores")
ranking = playerAtividadesService.get_ranking()

tab1, tab2 = st.tabs(['💠 Individual','💠 Todos'])   

with tab1:    
    next_col, back_col=  st.columns(2)
    placeholder = st.empty() #Cria placeholder.

    if next_col.button("Anterior", use_container_width=True):
        mover(-1, placeholder)

    if back_col.button("Próximo", use_container_width=True):
        mover(1, placeholder)

    try:    
        # jogador_nick_name = ranking["Nick Name"][st.session_state.indice]
        # jogador_pontos = ranking["Total de Pontos"][st.session_state.indice]
        placeholder.write(st.session_state.indice)
        #montar_imagem_jogador(background_path, avatar_path, jogador_nick_name, jogador_pontos, st.session_state.indice, placeholder)
        
    except FileNotFoundError:
        st.error("Arquivos de imagem não encontrados.")

with tab2:
    st.dataframe(ranking)
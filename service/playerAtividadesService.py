import pandas as pd
import repository.playerAtividadesRepository as playerAtividadesRepository

def get_ranking():
    atividades = playerAtividadesRepository.get_all()
    jogadores = {}  

    # Itera sobre os documentos e calcula o total de pontos por jogador
    for atividade in atividades:
        documento = atividade.to_dict()
        nick_name = documento.get("nick_name")
        pontos = documento.get("pontos", 0)  # Assume 0 pontos se não houver a chave 'pontos'

        if nick_name:  # Verifica se o nick_name existe
            if nick_name in jogadores:
                jogadores[nick_name] += pontos
            else:
                jogadores[nick_name] = pontos

    # Ordena os jogadores por total de pontos em ordem decrescente
    ranking = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)

    # Cria o DataFrame
    df_ranking = pd.DataFrame(ranking, columns=["Jogador", "Pontos"])
    df_ranking.index = range(1, len(df_ranking) + 1) # Modifica o índice do DataFrame

    return df_ranking


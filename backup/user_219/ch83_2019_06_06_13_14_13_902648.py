def media_por_inicial(entrada):
    saida={}
    for nome,media in entrada.items():
        saida[nome[0]]= media
    return saida
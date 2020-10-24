def medias_por_inicial(entrada):
    saida={}
    for nome,media in entrada.items():
        s= nome
        saida[s[0]]= media
    return saida
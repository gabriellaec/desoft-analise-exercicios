def medias_por_inicial(dicionario):
    resultado = {}
    for nomes,valores in dicionario.items():
        resultado[nomes[0]]=valores

    return resultado


            
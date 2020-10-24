def medias_por_inicial(dicionario):
    resultado = {}
    contador = {}
    for nomes,valores in dicionario.items():
        if nomes[0] not in resultado:
            resultado[nomes[0]]=valores
            contador[nomes[0]]=1
        else:
            resultado[nomes[0]]+=valores
            contador[nomes[0]]+=1

    for chave,valor in resultado.items():
        resultado[chave]=valor/contador[chave]
    return resultado
        


            
def medias_por_inicial(dicionario):
    resultado = {}
    dicionario_count = {}
    for nomes,valores in dicionario.items():
        if nomes[0] not in resultado:
            resultado[nomes[0]] = dicionario[nomes]
        else:
            resultado[nomes[0]] += dicionario[nomes]
            dicionario_count[nomes[0]] += 1
    for key,value in resultado.items():
        resultado[key]=value/dicionario_count[key]
        
    return resultado
        


            
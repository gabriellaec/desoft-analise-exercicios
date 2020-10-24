def medias_por_inicial(dicionario):
    resultado = {}
    dicionario_count = {}
    for i in dicionario.items():
        if i[0] not in resultado:
            resultado[i[0]] = dicionario[i]
        else:
            resultado[i[0]] += dicionario[i]
            dicionario_count[i[0]] += 1
    for key,value in resultado.items():
        resultado[key]=value/dicionario_count[key]
        
    return resultado
        


            
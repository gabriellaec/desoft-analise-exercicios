def medias_por_inicial(dicionario):
    resultado = {}
    dicionario_count = {}
    for nome in dicionario.items():
        if nome[0] not in resultado:
            resultado[nome[0]] = dicionario[nome]
            dicionario_count[nome[0]] = 1
        else:
            resultado[nome[0]] += dicionario[nome]
            dicionario_count[nome[0]] += 1
    for key,value in resultado.items():
        resultado[key]=value/dicionario_count[key]
        
    return resultado
        


            
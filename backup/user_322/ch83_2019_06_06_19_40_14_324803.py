def medias_por_inicial(n):
    dicionario = {}
    dicionario2 = {}
    lista = []
    for k,v in n.items():
        if k[0] in dicionario:
            dicionario[k[0]] += v
            dicionario2[k[0]] += 1
        else:
            dicionario2[k[0]] = 1
            dicionario[k[0]] = v
    for v2 in dicionario2.values():
        lista.append(v2)
        i = 0
    for k,v in dicionario.items():
        dicionario[k] = v/lista[i]
        i = i + 1
    return dicionario
     
            
            
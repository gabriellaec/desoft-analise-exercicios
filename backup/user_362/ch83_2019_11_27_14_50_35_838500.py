def media_por_inicial(x):
    qtd_letra = {}
    somas = {}    
    for i in x:
        
        if i[0] in qtd_letra:
            qtd_letra[i[0]] += 1
            somas[i[0]] += x[i]
    
        else:
            qtd_letra[i[0]] = 1
            somas[i[0]] = x[i]
    saida = {}
    for i in qtd_letra:
        saida[i] = somas[i]/qtd_letra[i]
    return saida
def interseccao_chaves(dicionario1, dicionario2):
    saida = []
    dic1 = []
    dic2 = []
    
    for k in dicionario1:
        dic1 = dicionario1[k]
    
    for k in dicionario2:
        dic2 = dicionario2[k]
    
    i=0
    while i >= len(dic1):
        
        if dic1[i] == dic2[i]:
            saida.append(dic1[i])
        else:
            return saida
        
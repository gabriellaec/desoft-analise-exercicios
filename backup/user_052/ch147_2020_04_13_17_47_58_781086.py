def mais_frequente (lista):
    dicionario = {}
    for i in lista:
        if i not in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] += 1
    a = list(dicionario.keys())
    b = list(dicionario.values())
    return a[b.index(max(b))]
    
        
        
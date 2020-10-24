def mais_frequente (lista):
    dicionario = {}
    for i in lista:
        if i not in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] += 1
    a = dicionario.values()
    for x in a:
        b = max(x)
        dicionario[i] = b
        return dicionario[i]
    
        
        
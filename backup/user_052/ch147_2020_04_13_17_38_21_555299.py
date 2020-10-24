def mais_frequente (lista):
    dicionario = {}
    for i in lista:
        if i not in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] += 1
    return dicionario
    a = dicionario.keys()
    lista = [a]
    return max(a)
        
        
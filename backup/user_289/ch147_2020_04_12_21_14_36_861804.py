def mais_frequente(lista):
    dicionario = {}
    for i in lista:
        if not i in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] += 1
    valormax = 0
    for value in dicionario:
        if value > valormax:
            valormax = value    
    return dicionario[valormarx]
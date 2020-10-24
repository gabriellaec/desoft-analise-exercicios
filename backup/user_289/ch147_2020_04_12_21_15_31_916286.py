def mais_frequente(lista):
    dicionario = {}
    for i in lista:
        if not i in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] += 1
    valormax = 0
    for n in dicionario:
        if n > valormax:
            valormax = n    
    return dicionario[valormarx]
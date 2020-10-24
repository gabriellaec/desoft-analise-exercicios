def mais_frequente(lista):
     dicionario = dict()
    for i in lista:
        if i in dicionario:
            dicionario[i] += 1
        else:
            dicionario[i] = 1
        if dicionario[i] > dicionario[i-1]:
            dicionario[i] = maior
    return maior
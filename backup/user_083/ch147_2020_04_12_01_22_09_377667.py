def mais_frequente(lista):
    dicionario={}
    for i in lista:
        if i in dicionario:
            dicionario[i]+=1
    return dicionario[i]
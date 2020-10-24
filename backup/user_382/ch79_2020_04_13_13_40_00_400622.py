def monta_dicionario (lista1,lista2):
    dicionario = dict()
    c = 0 
    for i in lista1:
        while True:
            dicionario[i] = lista2[c]
            c += 1
            break
    return dicionario
    
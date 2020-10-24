def monta_dicionario (lista1,lista2):
    dicionário = dict()
    c = 0
    for i in lista1:
        while c<len(lista1):
            dicionário[i] = lista2[c]
            c+=1
            break
    return dicionário

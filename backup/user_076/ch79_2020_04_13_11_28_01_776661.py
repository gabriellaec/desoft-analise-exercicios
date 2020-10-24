def monta_dicionario (lista_de_listas):
    lista_de_listas[0] = lista1
    lista_de_listas[1] = lista2
    dicionário = dict()
    c = 0
    for i in lista1:
        while c < len(lista1):
            dicionário[i] = lista2[c]
            c+=1
    return dicionário
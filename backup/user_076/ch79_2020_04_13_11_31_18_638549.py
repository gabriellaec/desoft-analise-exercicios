def monta_dicionario (lista_de_listas):
    dicionário = dict()
    c = 0
    for i in lista_de_listas[0]:
        while c < len(lista_de_listas[0]):
            dicionário[i] = lista_de_listas[1][c]
            c+=1
    return dicionário

def monta_dicionario(lista1,lista2):
    dicionario={}
    for e in lista1:
        for e_2 in lista2:
            dicionario[e]=e_2
    return dicionario
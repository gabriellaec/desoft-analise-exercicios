def monta_dicionario(lista1,lista2):
    dict={}
    for e in lista1:
        dict[e]=0
    for e in lista2:
        dict[lista1]=e
    return dict

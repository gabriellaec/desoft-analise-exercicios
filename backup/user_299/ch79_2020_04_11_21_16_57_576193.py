def monta_dicionario(lista1 , lista2):
    dicio = {}
    for i,e in enumerate(lista2):
        dicio[lista1[i]] = e
    return dicio
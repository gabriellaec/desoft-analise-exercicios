def monta_dicionario(lista1,lista2):
    dicionario = {}
    for i in lista1:
        for i2 in lista2:
            if i not in dicionario.keys() and i2 not in dicionario.values():
                dicionario[i]=i2
    return dicionario
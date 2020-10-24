def monta_dicionario(lista, lista2):
    
    dicionario = {}
    
    for i in range(0, len(lista)):
        dicionario[lista[i]] = lista2[i]
    return dicionario


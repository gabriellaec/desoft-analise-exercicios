def monta_dicionario(lista1, lista2):
    dicionario = {}
    
    while i < len(lista1):
        a = lista1[i]
        b = lista2[i]
        dicionario[a] = b

        i+=1

    return dicionario
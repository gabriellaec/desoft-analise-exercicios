def mais_frequente(lista):
    dicionario = {}
    for i in lista:
        if not i in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] += 1
    lista_values = dicionario.values()
    lista_keys = dicionario.keys()
    valor = 0
    for value in lista_values:
        if value > valor:
            valor = value    
    valor = lista_values[n]
    return lista_keys[n]
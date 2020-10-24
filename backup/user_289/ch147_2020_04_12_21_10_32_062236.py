def mais_frequente(lista):
    dicionario = {}
    for i in lista:
        if not i in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] += 1
    lista_values = []
    lista_values.append(dicionario.values())
    valormax = 0
    for value in lista_values:
        if value > valormax:
            valormax = value    
    valormax = lista_values[value]
    return valor
def mais_frequente(lista):
    dicionario = {}
    for i in lista:
        if not i in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] += 1
    lista_values = []
    lista_values.append(dicionario.values())
    valor_max = 0
    for value in lista_values:
        if value > valor:
            valor_max = value    
    valor = lista_values[value]
    return valor
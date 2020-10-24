def soma_impares(lista_inteira):
    t = 0
    lista_impares = []
    while t < len(lista_inteira):    #percorre a lista inteira e cria uma lista de impares
        if lista_inteira[t] % 2 != 0:
            lista_impares.append(lista_inteira[t])
        t += 1
    return sum(lista_impares)
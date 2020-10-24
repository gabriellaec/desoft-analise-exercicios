def soma_impares(lista):
    lista_impares = []
    contador = 0
    while contador < len(lista):
        if lista[contador] % 2 == 0:
            contador += 1
        else:
            lista_impares.append(lista[contador])
            contador += 1
    soma_impares = sum(lista_impares)
    return soma_impares
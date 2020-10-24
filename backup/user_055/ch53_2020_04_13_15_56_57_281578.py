def soma_impares(numeros):
    lista_impares = []
    lista_pares = []
    for n in numeros:
        if n % 2 == 0:
            lista_pares.append(n)
        else:
            lista_impares.append(n)
    return sum(lista_impares)

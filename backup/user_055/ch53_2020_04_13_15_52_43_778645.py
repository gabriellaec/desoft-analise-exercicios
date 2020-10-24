def soma_impares(numeros):
    lista_impares = []
    for n in numeros:
        if n % 2 == 0:
            break
        else:
            lista_impares.append(n)
    return sum(lista_impares)

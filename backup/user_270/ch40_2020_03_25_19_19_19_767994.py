def soma_valores(lista):
    soma = 0
    i = 0
    while i < len(lista):
        elemento = lista[i]
        soma += elemento
        i += 1
    return soma
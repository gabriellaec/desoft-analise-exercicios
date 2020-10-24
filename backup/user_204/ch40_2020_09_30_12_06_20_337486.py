def soma_valores(lista):
    valores = len(lista)
    i = 0
    soma = 0
    while i < valores:
        soma += lista[i]
        i += 1
    return soma
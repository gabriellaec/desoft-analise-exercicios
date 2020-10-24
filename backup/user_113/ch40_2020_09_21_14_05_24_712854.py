def soma_valores(lista):
    soma = 0
    x = 0
    while x <= len(lista):
        soma += lista[x]
        x += 1
    return soma
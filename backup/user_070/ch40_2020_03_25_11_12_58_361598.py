def soma_valores(lista):
    n = len(lista)
    i = 1
    soma = 0
    while i<=n:
        soma += lista[i-1]
        i += 1
    return soma
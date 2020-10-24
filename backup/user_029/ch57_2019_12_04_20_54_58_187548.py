def soma_impares(l1):
    soma = 0
    for i in range(len(l1)):
        if i%2 != 0:
            soma += i
    return soma
    
def soma_impares(l1):
    soma = 0
    for i in range(len(l1)):
        if l1[i]%2 > 0:
            soma += l1[i]
    return soma
    
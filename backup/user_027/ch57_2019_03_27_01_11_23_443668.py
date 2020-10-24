def soma_impares(x):
    soma = 0
    for i in x:
        if i%2 != 0:
            soma += i
    return soma
def soma_impares(n):
    soma = 0
    for i in n:
        if i%2 != 0:
            soma = soma + i
    return soma
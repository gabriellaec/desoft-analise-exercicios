def soma_impares(x):
    soma = 0
    while i < len(x):
        if x[i] % 2 == 0:
            i = i + 1
        else:
            soma = soma + x[i]
            i = i +1
    return soma
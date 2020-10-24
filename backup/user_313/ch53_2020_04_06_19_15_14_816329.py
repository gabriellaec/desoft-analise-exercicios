def soma_impares(l1):
    soma = 0
    for i in l1:
        if i % 2 != 0:
            soma = soma + i

    return soma
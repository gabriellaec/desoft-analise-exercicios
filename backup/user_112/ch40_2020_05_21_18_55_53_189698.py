def soma_valores(n):
    x = len(n)
    i = 0
    soma = 0
    while i < x:
        soma = soma + n[i]
        i += 1
    return soma
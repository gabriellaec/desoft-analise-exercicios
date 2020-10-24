def soma_valores(n):
    l = len(n)
    x = 0
    soma = 0
    while x < (l):
        soma = soma + int(n[x])
        x = x + 1
    return soma
    
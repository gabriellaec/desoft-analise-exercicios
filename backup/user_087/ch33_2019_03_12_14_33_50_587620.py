def funcao(x):
    soma = 0
    n = 1/(2**x)
    while x <= 99:
        soma = soma + n
        x = x + 1
    return soma

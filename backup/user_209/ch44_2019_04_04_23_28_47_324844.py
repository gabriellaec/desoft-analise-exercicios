def soma_valores (x):
    soma = 0
    i = 0
    while i < len(x):
        soma += x[i]
        i += 1
    return soma
v = [1,2,3,4]
resultado = soma_valores (v)
def soma_valores(v):
    i = 0
    soma = 0
    while i < len(v):
        soma += v[i]
        i += 1
    return soma
v=[3, 4, 7, 7, 5]
print(valores(v))
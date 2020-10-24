def valores(v):
    i = 0
    soma = 0
    while i < len(v):
        soma += v[i]
        i += 1
    return soma
a=[3, 4, 7, 7, 5]
print(valores(a))
def calcula_valor_devido(v, m, j):
    c = v * ((1+j)**m)
    return c
print(calcula_valor_devido(5, 6, 2))
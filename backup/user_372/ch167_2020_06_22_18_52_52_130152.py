def bairro_mais_custoso(gastos):
    dic1 = {}
    dic2 = {}
    for bairro, valor in gastos.items():
        dic1[bairro] = valor[6:12]
    for a, b in dic1.items():
        dic2[a] = sum(b)
    for i, j in dic2.items():
        if j == max(dic2.values()):
            return i
def bairro_mais_custoso(gastos):
    saida_1 = {}
    saida_2 = {}
    for x,y in gastos.items():
        saida_1[x] = y[6:12]
    for a,b in saida_1.items():
        saida_2[a] = sum(b)
    for i,j in saida_2.items():
        if j == max(saida_2.values()):
            return i
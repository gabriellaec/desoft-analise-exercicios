def bairro_mais_custoso(gastos):
    dic1 = {}
    dic2 = {}
    for bairro, valor in gastos.items():
        dic1[bairro] = valor[6:12]
    for bairro, valores in dic1.items():
        dic2[bairro] = sum(valores)
    for bairro, soma_valores in dic2.items():
        if bairro == max(dic2.values()):
            return soma_valores
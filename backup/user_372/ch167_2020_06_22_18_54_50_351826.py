def bairro_mais_custoso(gastos):
    dic1 = {}
    dic2 = {}
    for bairro, valor in gastos.items():
        dic1[bairro] = valor[6:12]
    for bairro1, valores in dic1.items():
        dic2[bairro1] = sum(valores)
    for bairro2, soma_valores in dic2.items():
        if bairro2 == max(dic2.values()):
            return soma_valores
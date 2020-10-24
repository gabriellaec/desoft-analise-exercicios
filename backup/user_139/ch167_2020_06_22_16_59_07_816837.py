def bairro_mais_custoso(dic):
    dic2 = {}
    for bairros, gastos in dic.items():
        semestre = 0
        for mes in range(6, 12):
            semestre += gastos[mes]
        dic2[bairros] = semestre
    nome = " "
    maior_gasto = 0
    for bairro, gasto in dic2.items():
        if gasto > maior_gasto:
            nome = bairro
            maior_gasto = gasto
    return nome

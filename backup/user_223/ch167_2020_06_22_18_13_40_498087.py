def bairro_mais_custoso(dicio):
    dic_total={}
    for bairro, gastos in dicio.items():
        gastos_totais = 0
        for mes in range (0, 11):
            gastos_totais += gastos[mes]
        dic_total[bairro] = gastos_totais
    return dic_total
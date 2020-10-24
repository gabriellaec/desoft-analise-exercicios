def total_do_semestre_por_bairro (dic):
    dic2 = {}
    for bairros, gastos in dic.items():
        semestre = 0
        for mes in range(6, 12):
            semestre += gastos[mes]
        dic2[bairros] = semestre
    return dic2

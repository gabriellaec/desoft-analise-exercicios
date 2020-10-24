def total_do_semestre_por_bairro(dicio):
    dic_total={}
    for bairro, gastos in dicio.items():
        semestre = 0
        for mes in range (6, 12):
            semestre += gastos[mes]
        dic_total[bairro] = semestre
    return dic_total
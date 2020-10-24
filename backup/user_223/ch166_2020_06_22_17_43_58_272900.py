def total_do_semestre_por_bairro(dicio):
    dic_total={}
    for bairro, gastos in dicio.items():
        for mes in range (6, 12):
            dic_total[bairro] = sum(gastos[mes])
    return dic_total
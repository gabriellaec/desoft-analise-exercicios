def total_do_semestre_por_bairro(dic):
    gastotot = {}
    for bairro, gastos in dic.items():
        semestre = 0
        for mes in range(6, 12):
            semestre += gastos[mes]
        gastotot[bairro] = semestre
    return gastotot
def total_do_semestre_por_bairro(dic):
    bairros = {}
    for bairro, gastos in dic.items():
        semestre = 0
        for mes in range(6, 12):
            semestre += gastos[mes]
        bairros[bairro] = semestre
    return bairros
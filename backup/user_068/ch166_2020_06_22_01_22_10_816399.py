def total_do_semestre_por_bairro(dicio):
    bairros = {}
    for bairro, gastos in dicio.items():
        semestre = 0
        for mes in range(6, 13):
            semestre += gastos[mes]
        bairros[bairro] = semestre
    return bairros


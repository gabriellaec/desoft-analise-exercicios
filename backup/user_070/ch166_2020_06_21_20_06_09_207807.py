def total_do_semestre_por_bairro(dicio):
    bairros = {}
    for bairro, gastos in dicio.items():
        semestre = 0
        for mes in range(6, 12)
            semestre += gastos[mes]
        bairros[bairro] = semestre
    return bairros
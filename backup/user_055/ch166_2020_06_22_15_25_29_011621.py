def total_do_semestre_por_bairro(bairros):
    gasto_semestre = {}
    for bairro, gasto in bairros.items():
        gastos = gasto[6:]
        gasto_semestre[bairro] = sum(gastos)
    return gasto_semestre
        
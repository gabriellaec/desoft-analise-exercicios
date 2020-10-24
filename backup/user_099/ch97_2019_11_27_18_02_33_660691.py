def total_do_semestre_por_bairro(gastos):
    gastos2 = {}
    for bairro,valores in gastos.items():
        total_6_meses = 0
        for i in range(6):
            total_6_meses += (list(valores)[len(valores)+i-6])
        gastos2[bairro]=total_6_meses
    return gastos2
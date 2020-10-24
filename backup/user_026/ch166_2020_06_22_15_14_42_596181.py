def total_do_semestre_por_bairro(gastos):
    gasto_total = {}
    for bairro in gastos:
        gasto_total[bairro] = 0
        for mes in gastos[bairro][6:]:
            gasto_total[bairro] +=mes
    return gasto_total
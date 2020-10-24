def total_do_semestre_por_bairro(gastos):
    gasto_total = {}
    for bairro in gastos:
        total = 0
        for i in range(12):
            valor = gastos[bairro]
            total += valor
        gasto_total[bairro] = total
    return gasto_total
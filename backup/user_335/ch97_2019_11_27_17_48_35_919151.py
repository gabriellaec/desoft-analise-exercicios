def total_do_semestre_por_bairro(gastos_infra):
    gasto_total = {}

    for bairro in gastos_infra:
        gastos = gastos_infra[bairro][6:12]
        gastototal = 0
        for i in range(len(gastos)):
            gastototal += gastos[i]

        gasto_total[bairro] = gastototal

    return gasto_total
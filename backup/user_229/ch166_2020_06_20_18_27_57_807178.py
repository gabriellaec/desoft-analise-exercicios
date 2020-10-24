def total_do_semestre_por_bairro(gastos_infraestrutura):
    gasto_total = {}
    for bairro, custos_lista in gastos_infraestrutura.items():
        total = 0
        for i in range(6, 12):
            valor = custos_lista[i]
            total += valor
        gasto_total[bairro] = total
    return gasto_total
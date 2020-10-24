def total_do_semestre_por_bairro(dic_gastos):
    gastos_6_meses = {}
    for bairro, lista_gastos in dic_gastos:
        if bairro not in gastos_6_meses.keys():
            gastos_6_meses[bairro] = 0
        else:
            for mes in range(5, 12):
                gasto = lista_gastos[mes]
                gastos_6_meses[bairro] += gasto
    return gastos_6_meses
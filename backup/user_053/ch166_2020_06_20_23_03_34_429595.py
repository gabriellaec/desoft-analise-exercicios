def total_do_semestre_por_bairro(dic_gastos):
    gastos_6_meses = {}
    for bairro, lista_gastos in dic_gastos.items():
        gastos_6_meses[bairro] = 0
        for mes in range(5, 12):
            gastos_6_meses[bairro] += lista_gastos[mes]
    return gastos_6_meses
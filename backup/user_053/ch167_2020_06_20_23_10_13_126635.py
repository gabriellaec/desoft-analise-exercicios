def total_do_semestre_por_bairro(dic_gastos):
    gastos_6_meses = {}
    for bairro, lista_gastos in dic_gastos.items():
        gastos_6_meses[bairro] = 0
        for mes in range(6, 12):
            gastos_6_meses[bairro] += lista_gastos[mes]
    return gastos_6_meses

def bairro_mais_custoso(dic_gastos):
    custo_bairro = total_do_semestre_por_bairro(dic_gastos)
    for bairro, custos in custo_bairro.items():
        if custos == max(custo_bairro.values()):
            return bairro
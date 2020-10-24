def total_do_semestre_por_bairro(bairros):
    gasto_semestre = {}
    for bairro, gasto in bairros.items():
        gastos = 0
        gastos = gasto[6:]
        print(gastos, sum(gastos))
        gasto_semestre[bairro] = sum(gastos)
    return gasto_semestre


def bairro_mais_custoso(bairros):
    gasto_semestre = total_do_semestre_por_bairro(bairros)
    maior_custo = 0
    mais_custoso = ''
    for bairro, custos in gasto_semestre.items():
        custo = 0
        custo += custos
        if custo > maior_custo:
            maior_custo = custo
            mais_custoso = bairro
    return mais_custoso
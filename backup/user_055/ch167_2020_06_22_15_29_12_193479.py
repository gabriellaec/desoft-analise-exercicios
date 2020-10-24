def total_do_semestre_por_bairro(bairros):
    gasto_semestre = {}
    for bairro, gasto in bairros.items():
        gastos = gasto[6:]
        print(gastos, sum(gastos))
        gasto_semestre[bairro] = sum(gastos)
    return gasto_semestre


def bairro_mais_custoso(bairros):
    gasto_semestre = total_do_semestre_por_bairro(bairros)
    maior_custo = 0
    mais_custoso = ''
    for bairro, custos in gasto_semestre.items():
        if custos > maior_custo:
            maior_custo = custos
            mais_custoso = bairro
    return mais_custoso
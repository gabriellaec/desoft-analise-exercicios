def total_do_semestre_por_bairro(bairros):
    bairros1 = {}
    for bairro, gastos in bairros.items():
        bairros1[bairro] = 0
        for mes in range(len(gastos)):
            if mes+1 > 6:
                bairros1[bairro] += gastos[mes]
    return bairros1

def bairro_mais_custoso(bairros):
    bairros1 = total_do_semestre_por_bairro(bairros)
    maiorcusto = 0
    for bairro, custo in bairros1.items():
        if custo > maiorcusto:
            maiorcusto = custo
            maiscustoso = bairro
    return maiscustoso
def total_do_semestre_por_bairro(dic):
    gastotot = {}
    for bairro, gastos in dic.items():
        semestre = 0
        for mes in range(6, 12):
            semestre += gastos[mes]
        gastotot[bairro] = semestre
    return gastotot

def bairro_mais_custoso(dic2):
    total = total_do_semestre_por_bairro(dic2)
    bairromaiscustoso = ''
    maximo = 0
    for bairro, custo in total.items():
        if custo > maximo:
            bairromaiscustoso = bairro
            maximo = custo
    return bairromaiscustoso
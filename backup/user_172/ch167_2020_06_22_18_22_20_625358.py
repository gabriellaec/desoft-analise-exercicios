def total_do_semestre_por_bairro(dic):
    bairros = {}
    for bairro,gastos in dic.items():
        semestre = 0
        for mes in range(6,12):
            semestre += gastos[mes]
        bairros[bairro] = semestre
    return bairros

def bairro_mais_custoso(dic):
    bairros = total_do_semestre_por_bairro(dic)
    mais = 0
    for bairro,custo in bairros.items():
        if custo>mais:
            mais = custo
            brabo = bairro
    return brabo
        
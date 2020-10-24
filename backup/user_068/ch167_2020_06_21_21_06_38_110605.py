 def total_do_semestre_por_bairro(dicio):
    bairros = {}
    for bairro, gastos in dicio.items():
        semestre = 0
        for mes in range(6, 12):
            semestre += gastos[mes]
        bairros[bairro] = semestre
    return bairros


def bairro_mais_custoso(dicio):
    bairros = total_do_semestre_por_bairro(dicio)
    recorde = 0
    o_bairro = ''
    for bairro, custo in bairros.items():
        if custo > recorde:
            recorde = custo
            o_bairro = bairro
    return o_bairro
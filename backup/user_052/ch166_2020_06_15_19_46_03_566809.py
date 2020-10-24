def total_do_semestre_por_bairro (empresa):
    novo = {}
    for bairro in empresa:
        novo[bairro] = 0
        for mes in empresa[bairro][6:]:
            novo[bairro] += mes
    return novo
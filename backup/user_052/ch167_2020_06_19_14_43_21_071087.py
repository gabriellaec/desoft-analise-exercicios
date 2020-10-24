def bairro_mais_custoso (empresa):
    novo = {}
    for bairro in empresa:
        novo[bairro] = 0
        for mes in empresa[bairro]:
            novo[bairro] += mes
    return max(novo)
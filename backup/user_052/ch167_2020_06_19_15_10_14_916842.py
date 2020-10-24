def bairro_mais_custoso (empresa):
    novo = {}
    for bairro in empresa:
        novo[bairro] = 0
        for mes in empresa[bairro][6:]:
            novo[bairro] += mes
    lista = []
    for i,e in novo.items():
        lista.append(e)
    x = max(lista)

    return x
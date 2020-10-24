def total_do_semestre_por_bairro(bairros):
    novo_dicionario = {}
    lista = []
    i = 6
    y = 0
    while i < 11:
        for nome in bairros.keys():
            y += bairros[nome][i]
            novo_dicionario[nome] = y
        i += 1
    return novo_dicionario
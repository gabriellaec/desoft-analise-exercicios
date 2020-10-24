def total_do_semestre_por_bairro(ano):
    dicionario={}
    for bairro in ano:
        dicionario[bairro]=sum(ano[bairro][:6])
    return dicionario

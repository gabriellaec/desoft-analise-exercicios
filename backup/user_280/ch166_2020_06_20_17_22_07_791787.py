def total_do_semestre_por_bairro(dicio_ano):
    dicio_semestre = {}
    for bairro, lista in dicio_ano.items():
        dicio_semestre[bairro] = lista[6:]
    dicio_soma6 = {}
    for bairro, lista in dicio_semestre.items():
        dicio_soma6[bairro] = sum(lista)
    return dicio_soma6
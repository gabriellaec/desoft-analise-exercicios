def total_do_semestre_por_bairro(dicio_ano):
    dicio_semestre = {}
    for bairro, lista in dicio_ano.items():
        dicio_semestre[bairro] = []
        dicio_semestre[bairro].append(lista[-6])
        dicio_semestre[bairro].append(lista[-5])
        dicio_semestre[bairro].append(lista[-4])
        dicio_semestre[bairro].append(lista[-3])
        dicio_semestre[bairro].append(lista[-2])
        dicio_semestre[bairro].append(lista[-1])
    dicio_soma6 = {}
    for bairro, lista in dicio_semestre.items():
        dicio_soma6[bairro] = sum(lista)
    return dicio_soma6
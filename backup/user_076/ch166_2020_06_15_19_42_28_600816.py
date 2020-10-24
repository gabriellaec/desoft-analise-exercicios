def total_do_semestre_por_bairro (d1):
    d2 = {}
    for bairro in d1:
        lista = d1[bairro]
        d2[bairro] = lista[6]+lista[7]+lista[8]+lista[9]+lista[10]+lista[11]
    return d2
def total_do_semestre_por_bairro(dicionario):
    dic = {}
    for bairro in dicionario:
        gasto = 0
        for a in range(6):
            gasto += dicionario[bairro]
            b = bairro
        dic[b] = gasto
    return dic
        
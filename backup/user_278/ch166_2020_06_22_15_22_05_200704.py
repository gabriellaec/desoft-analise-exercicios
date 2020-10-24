def total_do_semestre_por_bairro(dicionario):
    dic2 = {}
    for bairro in dicionario:
        dic2[bairro] = 0
        for valor in dicionario[bairro][6:]:
            dic2[bairro]+=valor
    return dic2
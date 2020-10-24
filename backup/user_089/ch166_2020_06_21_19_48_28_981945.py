def total_do_semestre_por_bairro(dicionario):
    dic2 = {}
    for k,v in dicionario.items():
        soma = 0
        dic2[k] = soma
        for e in v[6:]:
            soma += e
    return dic2
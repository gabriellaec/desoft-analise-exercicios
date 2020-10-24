def total_do_semestre_por_bairro(dic):
    for bairro, gastos in dic.items():
        dic[bairro] = sum(gastos[6:12])
    return dic

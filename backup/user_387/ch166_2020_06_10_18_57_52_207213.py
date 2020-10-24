def total_do_semestre_por_bairro(dic):
    dic_novo = {}
    for bairro in dic:
        dic_novo[bairro] = []
        for i in range(5,12):
            dic_novo[bairro].append(dic[bairro][i])
    return dic_novo
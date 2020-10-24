def total_do_semestre_por_bairro (dic):
    nova = []
    dic_novo = {}
    for i in dic:
        for o in dic[i][6:]:
            nova.append(o)
        soma = 0
        for w in nova:
            soma += w
        dic_novo[i] = soma 

    return dic_novo
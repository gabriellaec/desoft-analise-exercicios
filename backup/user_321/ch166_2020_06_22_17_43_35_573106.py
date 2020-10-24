def total_do_semestre_por_bairro(dic):
    k = {}
    for i in dic:
        for e in range(6,12):
            if not i in k:
                k[i] = dic[i][e]
            else:
                k[i] += dic[i][e]
    return k
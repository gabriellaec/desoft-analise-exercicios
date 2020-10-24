def total_do_semestre_por_bairro(dic):
    k = {}
    for i in dic:
        for e in range(6,12):
            k[i] += dic[i][e]
    return k
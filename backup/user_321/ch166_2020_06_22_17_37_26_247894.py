def total_do_semestre_por_bairro(dic):
    k = {}
    s = 0
    for i in dic:
        for e in range(6:12):
            s += dic[i][e]
        k[i] = s 
    return k
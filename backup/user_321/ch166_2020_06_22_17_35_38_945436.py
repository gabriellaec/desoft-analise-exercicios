def total_do_semestre_por_bairro(dic):
    k = 0
    for i in dic:
        k += dic[i][6:12]
    return k
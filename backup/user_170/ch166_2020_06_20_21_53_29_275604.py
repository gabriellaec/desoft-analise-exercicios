def total_do_semestre_por_bairro(dic):
    novoDic = {}
    for i in dic:
        gastoTotal = 0
        for v in range(7,12):
            gastoTotal += dic[i][v]
        novoDic[i] = gastoTotal
    return novoDic
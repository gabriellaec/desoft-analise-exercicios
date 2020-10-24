def total_do_semestre_por_bairro(dic):
    novoDic = {}
    for i in dic:
        gastoTotal = 0
        for v in range(6,len(dic[i])):
            gastoTotal += dic[i][v]
        novoDic[i] = gastoTotal
    return max(novoDic, key= novoDic.get)

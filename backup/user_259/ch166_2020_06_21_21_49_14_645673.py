def total_do_semestre_por_bairro(dic):
    gastos = dict()
    for bairro in dic:
        gastos[bairro] = 0
        for i in range(6,len(dic[bairro])):
            gastos[bairro] += dic[bairro][i]
    return gastos
        
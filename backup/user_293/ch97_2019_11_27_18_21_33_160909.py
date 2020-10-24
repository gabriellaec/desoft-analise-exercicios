def total_do_semestre_por_bairro(dic):
    gasto_total = dict()
    for e in dic:
        soma = 0
        for i in dic[e]:
            bairro = dic[e]
            soma += bairro[i]
        if not i in gasto_total:
            gasto_total[i] = soma
    return gasto_total[:7:-1]
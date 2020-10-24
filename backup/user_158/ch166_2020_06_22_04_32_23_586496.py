def total_do_semestre_por_bairro(dic):
    gasto_semestral ={}
    for bairo,gastos in dic.items():
        gasto_total = 0
        for i in range(6,len(gastos)):
            gasto_total += gastos[i]
        gasto_semestral[bairo] = gasto_total
    return gasto_semestral
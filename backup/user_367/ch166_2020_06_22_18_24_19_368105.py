def total_do_semestre_por_bairro(gastos):
    saida1 = dict()
    for x, y in gastos.items():
        saida1[x] = y[6:12]
    return saida1
        
def total_do_semestre_por_bairro(gastos):
    saida = dict()
    for x, y in gastos.items():
        saida[x] = y[6:12]
    return saida
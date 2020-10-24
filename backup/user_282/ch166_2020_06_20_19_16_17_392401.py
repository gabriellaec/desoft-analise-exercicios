def total_do_semestre_por_bairro(gastos):
    saida1 = dict()
    saida2 = dict()
    for x, y in gastos.items():
        saida1[x] = y[6:12]
    for a, b in saida1.items():
        saida2[a] = sum(b)
    return saida2
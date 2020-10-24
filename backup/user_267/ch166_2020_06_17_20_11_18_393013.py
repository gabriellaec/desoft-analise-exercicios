def total_do_semestre_por_bairro(dicio_gastos):
    gasto_total = {}
    for bairro, lista in dicio_gastos.items():
        i = 6
        numero = 0
        while i < len(lista):
            numero += lista[i]
            i += 1
        gasto_total[bairro] = numero
    return gasto_total
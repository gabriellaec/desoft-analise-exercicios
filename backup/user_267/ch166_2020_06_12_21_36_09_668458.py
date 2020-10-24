def total_do_semestre_por_bairro(dicio_gastos):
    gasto_total = {}
    i = 6
    numero = 0
    for bairro, lista in dicio_gastos.items():
        while i < len(lista):
            numero += lista[i]
            i += 1
        gasto_total[bairro] = numero
    return gasto_total
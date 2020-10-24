def total_do_semestre_por_bairro (gastos):
    gasto_semestral = {}
    for bairro in gastos:
        ultimo_sem_bairro = gastos[bairro][5:13] # lista com os gastos dos últimos 6 meses
        gasto_sem = 0
        for gasto in ultimo_sem_bairro:
            gasto_sem += gasto
        
        gasto_semestral[bairro] = gasto_sem
    return gasto_semestral
def total_do_semestre_por_bairro (gastos):
    gasto_semestral = {}
    for bairro in gastos:
        ultimo_sem_bairro = gastos[bairro][6:] # lista com os gastos dos últimos 6 meses
        gasto_sem = 0
        for gasto in ultimo_sem_bairro:
            gasto_sem += gasto
        
        gasto_semestral[bairro] = gasto_sem
    return gasto_semestral

def bairro_mais_custoso(gastos):
    gasto_semestral = total_do_semestre_por_bairro (gastos)
    b_m_gasta = ''
    gasto_max = 0
    for bairro, gasto in gasto_semestral.items():
        if gasto> gasto_max:
            gasto_max = gasto
            b_m_gasta = bairro
            
    return b_m_gasta
def total_do_semestre_por_bairro(gastos):
    return {bairro : sum(gastos[bairro][6:]) for bairro in gastos}

def bairro_mais_custoso(gastos):
    gastos_sem = total_do_semestre_por_bairro(gastos)
    return max(gastos_sem,key=gastos_sem)
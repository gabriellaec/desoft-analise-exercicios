def total_do_semestre_por_bairro(gastos):
    return {bairro : sum(gastos[bairro][7:]) for bairro in gastos}

def bairro_mais_custoso(gastos):
    return max(total_do_semestre_por_bairro(gastos),key=gastos.get)
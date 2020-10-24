def total_do_semestre_por_bairro(gastos):
    return {bairro : sum(gastos[bairro][6:]) for bairro in gastos}
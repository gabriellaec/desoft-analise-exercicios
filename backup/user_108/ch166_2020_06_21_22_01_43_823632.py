def total_do_semestre_por_bairro(gastos):
    return {bairro : gastos[bairro][7:] for bairro in gastos}
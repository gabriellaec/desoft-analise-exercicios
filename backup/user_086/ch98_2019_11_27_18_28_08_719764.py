def bairro_mais_custoso(gastos):
    dicio_gtotal = total_do_semestre_por_bairro(gastos)
    gastomaior = 0
    mais_custoso = '.'
    for k in dicio_gtotal.keys():
        if dicio_gtotal[k]>gastomaior:
            dicio_gtotal[k] = gastomaior
            mais_custoso = k
    return mais_custoso
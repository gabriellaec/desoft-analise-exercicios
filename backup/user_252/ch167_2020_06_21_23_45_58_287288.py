def total_do_semestre_por_bairro(dicio):
    custo_total={}
    for bairro, custo in dicio.items():
        total=0
        for mes in range(6, 12):
            total+=custo[mes]
            custo_total[bairro]=total
    return custo_total
def bairro_mais_custoso(infra):
    novo=total_do_semestre_por_bairro(infra)
    mais_gasto=0
    for bairro, total in novo.items():
        if total>mais_gasto:
            mais_gasto=total
            custoso=bairro
    return custoso
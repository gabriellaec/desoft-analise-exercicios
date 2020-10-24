def total_do_semestre_por_bairro(dicio):
    custo_total={}
    for bairro, custo in dicio.items():
        total=0
        for mes in range(6, 12):
            total+=custo[mes]
            custo_total[bairro]=total
    return custo_total
            
            
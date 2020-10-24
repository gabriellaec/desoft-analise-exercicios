def total_do_semestre_por_bairro(infraestrutura):
    gasto_total = {}
    for bairro in infraestrutura:
        for mes in range(6,12):
            if bairro not in gasto_total:
                gasto_total[bairro] = infraestrutura[bairro][mes]
            else:
                gasto_total[bairro] += infraestrutura[bairro][mes]
    return gasto_total
def total_do_semestre_por_bairro(bairros):
    bairros1 = {}
    for bairro, gastos in bairros.items():
        bairros1[bairro] = 0
        for mes in gastos:
            if mes+1 > 6:
                bairros1[bairro] += mes
    return bairros1
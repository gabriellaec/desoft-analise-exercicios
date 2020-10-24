def total_do_semestre_por_bairro (dicionario):
    bairros = {}
    for bairro, gastos in dicionario.items():
        semestre = 0
        for mes in range(6,12):
            semestre += gastos[mes]
        bairros[bairro] = semestre
    return bairros    
            
    
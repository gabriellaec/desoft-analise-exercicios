def mais_populoso(dic_estados):
    maior_pop = 0
    estado_mais_pop = ''
    for estado, municipios in dic_estados.items():
        pop_total = 0
        for populacao in municipios.values():
            pop_total += populacao
        if pop_total > maior_pop:
            maior_pop = pop_total
            estado_mais_pop = estado
    return estado_mais_pop
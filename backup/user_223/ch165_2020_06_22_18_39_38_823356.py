def mais_populoso(dicio):
    maior_pop = 0
    for estado, cidades in dicio.items():
        for pop in cidades.values():
            pop_total = sum(pop)
        if pop_total > mais_pop:
            maior_pop = pop_total
            mais_pop = estado
    return estado
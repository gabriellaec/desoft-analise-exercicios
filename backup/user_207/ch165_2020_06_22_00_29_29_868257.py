def mais_populoso (brasil):
    new_dicio = {}
    for estado, dicio in brasil.items():
        pop_estado = 0
        for pop in dicio.values():
            pop_estado += pop
        new_dicio[estado] = pop_estado
    
    max_pop = 0
    mais_pop = ''
    for estado, pop in new_dicio.items():
        if pop > max_pop:
            max_pop = pop
            mais_pop = estado
    return mais_pop 
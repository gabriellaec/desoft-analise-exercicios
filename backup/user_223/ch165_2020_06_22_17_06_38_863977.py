def mais_populoso(dicio):
    mais_pop = 0
    for v in dicio.values():
        for hab in v.values():
            pop = sum(hab)
            if pop > mais_pop:
                mais_pop = pop
    return mais_pop
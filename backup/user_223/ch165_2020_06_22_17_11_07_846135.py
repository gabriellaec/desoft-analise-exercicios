def mais_populoso(dicio):
    mais_pop = 0
    for k, v in dicio.items():
        pop = sum(dicio[k][v])
        if pop > mais_pop:
            mais_pop = pop
    return mais_pop
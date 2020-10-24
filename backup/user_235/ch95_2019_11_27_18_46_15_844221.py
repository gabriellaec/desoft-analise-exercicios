def mais_populoso(dictio):
    pop=[]
    dicio2=dictio.values()
    for i in dicio2:
        pop[i] = dicio2[i]
    melhor_pop = 100000000000000
    for z in pop:
        if pop[i] < melhor_pop:
            melhor_pop = pop[i]
    return melhor_pop
def mais_populoso(dic_estados):
    dic_pop = {}
    for estado, dic_cidades in dic_estados.items():
        for populaçao in dic_cidades.values():
            dic_pop[estado] += populaçao
    maior_pop = 0
    for estado, pop in dic_pop.items():
        if pop > maior_pop:
            maior_pop = pop
            state = estado
    return state
    
        
    
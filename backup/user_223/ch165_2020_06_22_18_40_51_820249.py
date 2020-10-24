def mais_populoso(dicio):
    maior_pop = 0
    for estado, cidades in dicio.items():
        populacao = 0
        for pop in cidades.values():
            populacao == pop
        if populacao > mais_pop:
            maior_pop = populacao
            mais_pop = estado
    return estado
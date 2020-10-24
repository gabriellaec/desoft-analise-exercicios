def mais_populoso(pais):
    pop_total ={}
    for estado,municipios in pais.items():
        soma = 0
        for cidade, pop in municipios.items():
            soma += pop
        pop_total[estado]=soma
    max = list(pop_total.values())[0]
    for estado,populacao in pop_total.items():
        if max <= populacao:
            max = populacao
            est_populoso = estado
	return "{0} é o estado mais populoso de todos.".format(est_populoso)
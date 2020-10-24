def mais_populoso(estados_municipios_habitantes):
    mais = ''
    maior = 0
    for estado, municipios_dict in estados_municipios_habitantes.items():
        pop = 0
        for populacao in municipios_dict.values():
            pop += populacao
        if pop > maior:  
            maior = pop
            mais = '{}'.format(estado)
    return mais
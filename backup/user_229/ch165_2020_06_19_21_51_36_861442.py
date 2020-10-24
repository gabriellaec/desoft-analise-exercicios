def mais_populoso(estados_municipios_habitantes):
    mais = ''
    maior = 0
    for estado in estados_municipios_habitantes:
        pop = 0
        for municipios in estado[0]:
            pop += municipios[0]
        if pop > maior:  
            maior = pop
            mais = '{}'.format(estado)
    return mais
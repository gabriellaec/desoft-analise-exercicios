def mais_populoso(dic_estados):
    maior = 0    
    mais_pop = ''
    for estado in dic_estados.keys():
        for cidade, populaçao in dic_cidades[estado].items():
            pop = sum(dic_estados[estado].values())
        if pop > maior:
            maior = pop
            mais_pop = estado
    return mais_pop
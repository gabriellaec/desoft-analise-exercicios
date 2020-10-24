def mais_populoso(brasil):
    populacao = 0
    for i in brasil:
        pop = 0
        for cidade in brasil[estado]:
            pop += brasil[estado][cidade]
        if pop> populacao:
            populacao = pop
            esta_pop = estado
    return esta_pop
            
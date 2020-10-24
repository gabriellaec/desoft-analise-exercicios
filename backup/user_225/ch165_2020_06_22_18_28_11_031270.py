def mais_populoso(brasil):
    maispop = 0
    for estado in brasil:
        pop = 0
        for cidade in brasil[estado]:
            pop += brasil[estado][cidade]
        if pop > maispop:
            maispop = pop
            est_mp = estado
    return est_mp
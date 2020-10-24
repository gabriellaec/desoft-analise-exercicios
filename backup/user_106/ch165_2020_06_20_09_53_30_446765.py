def mais_populoso(brasil):
    pop = 0
    for estado in brasil:
        for cidade in brasil[estado]:
            pop += brasil[estado][cidade]
        if pop > maispop:
            maispop = pop
            est_mp = brasil[estado]
    return est_mp
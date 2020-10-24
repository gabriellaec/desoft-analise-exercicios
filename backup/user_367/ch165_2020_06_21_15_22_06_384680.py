def mais_populoso(brasil):
    mais_populoso = 0
    for i in brasil:
        populacao = 0
        for cidade in brasil[estado]:
            populacao += brasil[estado][cidade]
        if populacao> mais_populoso:
            mais_populoso = populacao
            esta_populoso = estado
    return esta_populoso
            
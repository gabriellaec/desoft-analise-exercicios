def calcula_tempo(dicio):
    dict={}
    for nome, acc in dicio.items():
        dict[nome] = (200/acc)**0.5
    return dict
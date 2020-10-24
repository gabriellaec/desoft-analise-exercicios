def calcula_tempo(d):
    new_d = {}
    for key,a in d.items():
        tempo = (200/a)**(1/2)
        new_d[key] = tempo
    return new_d
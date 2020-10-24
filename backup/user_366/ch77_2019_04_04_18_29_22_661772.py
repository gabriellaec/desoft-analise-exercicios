def calcula_tempo(atletas):
    tempos = {}
    for k, v in atletas.items():
        v = (200/v)**(1/2)
        tempos[k] = v
    return tempos
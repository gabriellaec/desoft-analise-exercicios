def calcula_tempo(atletas):
    tempos = {}
    for k,v in atletas.items():
        tempos[k] = (200/v)**(0.5)
    return tempos
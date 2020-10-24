def calcula_tempo(atletas):
    for i in atletas:
        aceleracao = atletas.values()
        tempo = (200/aceleracao)**(1/2)
        tempos = {}
        tempos.keys() = atletas.keys()
        tempos.values()=tempo
    return tempos
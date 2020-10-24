def calcula_tempo(atletas):
    tempos = {}
    for nomes in atletas:
        aceleracao = atletas[nomes]
        tempo = (200/aceleracao)**(1/2)
        tempos[nomes]=tempo
    return tempos
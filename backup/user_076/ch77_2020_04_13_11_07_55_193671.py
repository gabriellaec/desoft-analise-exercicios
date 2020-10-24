def calcula_tempo(nomes_aceleração):
    nomes_tempo = dict()
    for i in nomes_aceleração:
        t = (200/nomes_aceleração[i])**(1/2)
        nomes_tempo[i] = t
    return nomes_tempo
        
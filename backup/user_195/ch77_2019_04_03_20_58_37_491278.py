def calcula_tempo(D):
    C={}
    for nomes,tempo in D.items():
        t=tempo
        a=(200-2*t)/t**2
        C[nomes]=a
    return C

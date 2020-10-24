def calcula_tempo(x):
    tempo = {}
    for i, e in x.items():
        d = ((2*100)/e)**(1/2)
        tempo[i] = d
    return tempo
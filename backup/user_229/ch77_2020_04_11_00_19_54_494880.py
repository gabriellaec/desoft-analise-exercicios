def calcula_tempo(a):
    tempo = dict()
    for i in a:
        tempo[i] = (200/a[i])**(1/2)
    return tempo
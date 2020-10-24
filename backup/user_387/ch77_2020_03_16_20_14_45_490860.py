def calcula_tempo(a):
    for atleta in a:
        a[atleta] = (0.1/float(a[atleta]))**0.5
    return a
        
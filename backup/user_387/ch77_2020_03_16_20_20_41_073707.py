def calcula_tempo(a):
    for atleta in a:
        a[atleta] = (0.100/a[atleta])**0.5
    return a
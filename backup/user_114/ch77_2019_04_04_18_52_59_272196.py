def calcula_tempo(d1):
    d2={}
    for atletas, aceleracao in d1.items():
        t=(200/aceleracao)**(1/2)
        d2[atletas]=t
    return d2
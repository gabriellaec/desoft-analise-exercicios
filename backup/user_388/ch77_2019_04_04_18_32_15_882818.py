def calcula_tempo(d1):
    d2={}
    for atleta, acelerac in d1.items():
        t = (200/acelerac)**0.5
        d2[atleta]= t
    return d2
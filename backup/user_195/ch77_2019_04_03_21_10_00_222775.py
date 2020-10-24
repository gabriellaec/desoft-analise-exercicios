def calcula_tempo(D):
    C={}
    for nomes,aceleracao in D.items():
        a=aceleracao
        t=(200/a)**1/2
        C[nomes]=t
    return C

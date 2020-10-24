def calcula_tempo(dicio):
    dicio2={}
    for i in dicio.values():
        t=(200/i)**0.5
        for b in dicio:
            if dicio[b]==i:
                dicio2[b]=t
    return dicio2
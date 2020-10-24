def calcula_tempo(dicio):
    dicio2 = {}
    for i,j in dicio.items():
        dicio2[i] = (2*100/j)**.5
        
    return dicio2
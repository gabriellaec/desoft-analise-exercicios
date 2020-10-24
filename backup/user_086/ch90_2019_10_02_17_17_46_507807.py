#h1 e h2 são strings
def segundos_entre(h1,h2):
    h1h=int(h1[0:2])
    h2h=int(h2[0:2])
    h1m=int(h1[3:5])
    h2m=int(h2[3:5])
    h1s=int(h1[6:8])
    h2s=int(h2[6:8])
    difh=h2h-h1h
    difm=h2m-h1m
    difs=h2s-h1s
    diftotal=difh*60*60+difm*60+difs
    return diftotal
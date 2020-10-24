import math

def snell_descartes (n1,n2,teta1):
    teta1rad = (math.pi *teta1)/180
    (n1/n2) = (math.sin(teta1rad) / math.sin(teta2rad))
    teta2graus = (180 *teta2rad)/math.pi
    return teta2graus
    
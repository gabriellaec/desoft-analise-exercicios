import math
def snell_descartes(n1, n2, teta1):
    senoteta2 = n1*math.sin(teta1*math.pi/180)
    teta2 = math.asin(senoteta2)
    teta2 = 180*teta2/math.pi
    return teta2
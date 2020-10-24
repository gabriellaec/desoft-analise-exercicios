import math
def snell_descartes(n1,n2,teta1):
    teta1*=math.pi/180
    senot2 = n1/n2*(math.sin(teta1))
    t2 = (math.asin(senot2))*(180/math.pi)
    return t2
    
import math
def snell_descartes (n1, n2, teta1) :
    y = -n1*(math.sin(teta1*180/math.pi)/n2)
    return y 
from math import*
def snell_descartes(n1, n2, teta1):
    teta1 = math.radians(teta1)
    teta2 = math.radians(teta2)
    teta2= (n1*sin(teta1))/n2
    teta2=sin(teta2)
    return teta2
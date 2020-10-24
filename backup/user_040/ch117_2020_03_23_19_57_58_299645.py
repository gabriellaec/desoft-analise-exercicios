from math import radians
def snell_descartes(n1,n2,teta1):
    return radians(n1*radians(teta1)/n2)
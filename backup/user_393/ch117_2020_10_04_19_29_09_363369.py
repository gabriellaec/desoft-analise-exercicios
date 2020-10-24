import math

def snell_descartes(n1,n2,teta1):
    teta2= asin((n1/n2)*sin(teta1))
    return teta2

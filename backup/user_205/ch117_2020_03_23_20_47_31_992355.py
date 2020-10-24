from math import sin, pi 

def snell_descartes (n1,n2,a1):
    af = a1*(180°/pi)
    y = (n1*(sin(af))/n2)*pi/180
    return y
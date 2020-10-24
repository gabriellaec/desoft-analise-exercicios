from math import sin, pi 

def snell_descartes (n1,n2,a1):
    y = (n1*(sin(a1)*180/pi)/n2)*pi/180
    return y
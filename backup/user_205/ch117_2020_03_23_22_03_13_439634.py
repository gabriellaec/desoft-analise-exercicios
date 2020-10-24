from math import sin, pi, radians, degrees, asin
def snell_descartes (n,p,a):
    x = (n*sin(radians(a)))/p #valor do seno 
    y = asin(x) #função inversa pra saber o angulo em radianos
    grau = degrees(y) #passando para graus
    return grau
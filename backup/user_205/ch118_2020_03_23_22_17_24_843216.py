from math import sin, pi, radians, degrees, asin
def reflexao_total_interna(n,p,a):
    x = (p*sin(radians(a)))/n #valor do seno
    y = degrees(x)
    if y>1:
        return True
    else:
        return False
   
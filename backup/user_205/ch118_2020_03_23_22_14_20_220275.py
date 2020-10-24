from math import sin, pi, radians, degrees, asin
def reflexao_total_interna(n,p,a):
    x = (p*degrees(sin(radians(a))))/n #valor do seno 
    if x>1:
        return True
    else:
        return False
   
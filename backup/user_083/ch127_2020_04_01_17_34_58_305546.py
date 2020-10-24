import math
def calcula_elongacao(t,a,w,y):
    b=math.radians(w)
    c=math.radians(y)
    r=y+(b*t)
    z=math.cos(r)
    g=math.degrees(z)
    x=a*(g)
    return x
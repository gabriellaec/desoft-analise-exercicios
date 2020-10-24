import math
def calcula_elongacao(t,a,w,y):
    t=1
    b=math.radians(w)
    a=1
    c=math.radians(y)
    r=y+(b*t)
    z=math.cos(r)
    g=math.degrees(z)
    x=a*(g)
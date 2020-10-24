import math
def  snell_descartes(x,y,z):
    a=math.radians(z)
    b=math.sin(a)
    n=x*z/y
    d=math.asin(n)
    e=math.degrees(d)
    return n

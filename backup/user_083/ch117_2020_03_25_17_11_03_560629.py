import math
def  snell_descartes(x,y,z,n):
    z=math.asin(z)
    n=math.asin(n)
    n=x*z/y
    return n
a=0
b=10
c=0
d=math.asin(c)
e=30
f=math.asin(e)
g=a*d/b
h=math.degrees(g)
print(h)
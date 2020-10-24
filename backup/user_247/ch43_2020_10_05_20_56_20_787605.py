import math
def snell_descarrtes (n1, n2, x):
    xr= math.radians(x)
    y= math.asin((math.sin(xr)*n1/n2))
    yr= math.degrees(y)
    return yr

n1= 10
n2= 5
x= 30
a= snell_descartes(n1, n2, x)

print(a)

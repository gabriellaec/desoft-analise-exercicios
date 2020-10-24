import math
def snell_descartes(n1,n2,x):
    y=(n1/n2)*(math.radians(x))
    z=math.degrees(y)
    return z
print(snell_descartes(1,2,30))
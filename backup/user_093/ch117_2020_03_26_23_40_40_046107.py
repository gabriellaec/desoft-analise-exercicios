import math
def snell_descartes(n1,n2,x):
    y=(n1/n2)*(math.sin(math.radians(x)))
    z=math.radians(y)
    return z
print(snell_descartes(1,2,30))
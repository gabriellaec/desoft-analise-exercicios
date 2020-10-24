import math
def snell_descartes(n1,n2,x):
    y=(n1/n2)*(math.sin(x))
    z=math.sin(y)
    return z
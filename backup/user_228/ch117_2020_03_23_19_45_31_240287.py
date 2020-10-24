import math
def snell_descartes(n,m,s):
    a=n*s/math.sin(math.radians(m))
    a=math.sin(math.radians(a))
    return(a)


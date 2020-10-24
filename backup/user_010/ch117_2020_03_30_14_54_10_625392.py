import math
n1=1
n2=2
ang1=30
def snell_descartes (a, b, c):
    
    y = (a*math.sin(math.radians(c)))/b
    z= math.asin (y)
    return math.degrees (z)
ang2=snell_descartes (n1, n2, ang1)
print (ang2)
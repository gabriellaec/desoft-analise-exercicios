import math

def snell_descartes(n1, n2, ang1):
    sinang2 = (math.sin(math.degrees(ang1))*(n1/n2))
    x = math.asin(sinang2)
    y = math.degrees(x) 
    return (y)
    
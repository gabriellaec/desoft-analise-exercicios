import math

def snell_descartes(x,y,z):

    a = math.radians(z)
    teta2 = (x/y)*a
    return math.radians(teta2)


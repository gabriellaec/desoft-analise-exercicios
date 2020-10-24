import math

def snell_descartes(x,y,z):

    # a = math.radians(z)
    teta2 = (x/y)*z
    return math.radians(teta2)
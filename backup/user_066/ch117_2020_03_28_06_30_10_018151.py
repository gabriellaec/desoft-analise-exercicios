import math
def snell_descartes(n1, n2, teta1):
    teta1 = math.radians(teta1)
    senoteta2 = n1*math.sin(teta1)
    teta2 = math.asin(senoteta2)
    teta2 = math.degrees(teta2)
    return teta2
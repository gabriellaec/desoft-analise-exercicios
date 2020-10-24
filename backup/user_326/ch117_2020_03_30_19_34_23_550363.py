import math
def snell_descartes(n1, n2, angulo1):
    seno2 = n1 * math.sin(math.radians(angulo1)) / n2
    angulo2 =math.degrees(math.asin(seno2))
    return angulo2  
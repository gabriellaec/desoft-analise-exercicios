import math
def snell_descartes(n1, n2, angulo1):
    seno1 = math.sin(math.radians(angulo1))
    seno2 = (n1/n2)*seno1
    return seno 2
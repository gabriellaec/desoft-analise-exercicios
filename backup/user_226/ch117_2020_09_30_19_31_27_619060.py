import math

def snell_descartes(n1, n2, a1):
    primeira_pt_equacao = n1/n2
    a1 = math.radians(a1)
    x = math.sin(a1) * primeira_pt_equacao
    a2 = math.asin(x)
    a2 = math.degrees(a2)
    return a2
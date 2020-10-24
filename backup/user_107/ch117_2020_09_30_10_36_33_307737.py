import math

def deg_to_rad (degrees):
    return degrees * math.pi / 180

def snell_descartes (n1, n2, tetta1):
    return n1 / n2 * math.sin(deg_to_rad(tetta1))

import math

def deg_to_rad (degrees):
    return degrees * math.pi / 180

def rad_to_deg (radians):
    return radians * 180 / math.pi

def snell_descartes (n1, n2, tetta1):
    sin_tetta1 = math.sin(deg_to_rad(tetta1))
    sin_tetta2 = n1 / n2 * sin_tetta1
    
    return rad_to_deg(math.asin(sin_tetta2))

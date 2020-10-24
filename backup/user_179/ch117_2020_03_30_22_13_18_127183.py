import math
def snell_descartes (n1,n2,teta1):   
    teta1_radianos = math.radians(teta1)
    
    math.sin(teta2) = n1 * math.sin(teta1_radianos)/n2
    a = math.asin(math.sin(teta2))
    teta2_angulo = math.degrees(a)
    return teta2_angulo
    
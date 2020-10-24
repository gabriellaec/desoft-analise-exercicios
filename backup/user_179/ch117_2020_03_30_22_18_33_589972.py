import math
def snell_descartes (n1,n2,teta1):   
    teta1_radianos = math.radians(teta1)
    
    teta2 = math.asin(n1 * math.sin(teta1_radianos)/n2)
    
    teta2_angulo = math.degrees(teta2)
    
    return teta2_angulo
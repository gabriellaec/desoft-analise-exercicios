import math

def snell_descartes (n1,n2,teta1):
    if teta1 == 0:
        teta2=0
    else:
        math.sin(teta2) = (n1/n2) * math.sin(math.radians(teta1))
    return math.degrees(teta2)
    
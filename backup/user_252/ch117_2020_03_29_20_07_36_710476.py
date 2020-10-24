import math
def snell_descartes(n1,n2,o1):
    sin_o2=(n1*math.sin(math.radians(o1)))/n2
    if sin_o2>1:
        return True
    else:
        return False
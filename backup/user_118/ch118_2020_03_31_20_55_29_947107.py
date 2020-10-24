import math
def snell_descartes(n1,n2,o1):
    o2=math.asin((n1*math.sin(math.radians(o1)))/n2)
    return (math.degrees(o2))
import math
def reflexao_total_interna(n2,teta2,n1):
    teta1=math.sin((n2*math.sin(math.radians(teta2)))/n1)
    return teta1
    if teta1>1:
        return True
    else:
        return False
    

import math
def snell_descartes(n1,n2,teta1):
    teta2s = math.sin(math.radians(teta1))*n1/n2 
    teta2 = math.asin(teta2s)
    return math.degrees(teta2)
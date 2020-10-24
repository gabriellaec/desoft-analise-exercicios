import math 
def snell_descartes(n1, n2, O1):
    seno2 = (n1/n2)*math.sin(math.radians(O1))
    return math.degrees(seno2)
    
import math 
def snell_descartes(n1, n2, O1):
    seno2 = (n1/n2)*math.sin(O1)
    return math.degrees(seno2)
    
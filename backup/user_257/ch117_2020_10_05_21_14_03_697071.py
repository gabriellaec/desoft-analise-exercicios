import math
# math.asin
def snell_descartes(n1,n2,O1):
    O2= math.asin(n1*math.sin(math.radians(O1))/n2)
    transformar_em_graus= math.degrees(O2)
    return transformar_em_graus
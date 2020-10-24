import math
def snell_descartes(n1, n2, teta1):
    teta1= math.radiana(teta1)
    teta2= math.asin( n1 * math.sin(teta1)/n2)
    teta2= math.degrees(teta2)
import math

def snell_descartes(n1, n2, teta1):
    teta1 = math.radians(teta1)
    teta2 = n1*(math.sin(teta1))/n2
    teta2 = math.degrees(teta2)
    return x
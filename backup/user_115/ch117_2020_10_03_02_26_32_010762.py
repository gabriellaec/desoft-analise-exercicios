import math

def snell_descartes(n1, n2, t1):
    t2 = math.asin((n1*math.sin(t1)/n2))
    graus = (t2*180)/math.pi
    print(graus)

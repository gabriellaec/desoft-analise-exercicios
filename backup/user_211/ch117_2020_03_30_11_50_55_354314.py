import math

def snell_descartes(n1,n2,teta):
    n1=float(input("n1:\n"))
    n2=float(input("n2:\n"))
    teta=math.degrees(input("teta:\n"))
    sent2=((n1*math.degrees(math.sin(teta)))/(n2))
    return math.degrees(math.asin(sent2))


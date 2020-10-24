import math

def snell_descartes():
    n1=int(input("n1:\n"))
    n2=int(input("n2:\n"))
    teta=math.degrees(input("teta:\n"))
    sent2=((n1*math.degrees(math.sin(teta)))/(n2))
    return math.degrees(math.asin(sent2))
import math

def snell_descartes(n1,n2,teta):
    n1=input("n1:"))
    n2=input("n2:"))
    teta=input(math.degrees("teta:"))
    sent2=((n1*math.degrees(math.sin(teta)))/(n2))
    return math.degrees(math.asin(sent2))

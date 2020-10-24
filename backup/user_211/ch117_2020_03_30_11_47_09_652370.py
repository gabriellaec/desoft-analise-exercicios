import math

def snell_descartes(n1,n2,teta):
    sent2=((n1*math.degrees(math.sin(teta)))/(n2))
    return math.degrees(math.asin(sent2))
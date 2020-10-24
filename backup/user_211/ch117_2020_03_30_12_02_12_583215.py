import math

def snell_descartes(n1,n2,teta):
    sent2=((n1*math.sin(math.degrees(teta)))/(n2))
    return math.degrees(math.asin(sent2))

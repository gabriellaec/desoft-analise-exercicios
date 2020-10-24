import math

def snell_descartes(n1,n2,teta1):
    seno=(n1)*(1/n2)*(math.sin(math.radians(teta1)))
    x=math.asin(seno)
    return x



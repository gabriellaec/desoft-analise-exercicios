import math

def snell_descartes(n1,n2,teta1):
    teta1Rad=math.radians(teta1)
    senteta2=(n1/n2)*math.sin(teta1Rad)
    teta2Rad=math.asin(senteta2)
    math.radians(teta2)=teta2Rad
    return teta2
import math

def snell_descartes(teta1graus, n1,n2):
    teta1rad = math.radians(teta1graus)
    senteta2rad = (n1*math.sin(teta1rad))/n2
    teta2rad = math.asin(senteta2rad)
    teta2graus = math.degrees(teta2rad)
    return teta2graus
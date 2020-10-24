import math

def reflexao_total_interna(n1,n2,teta2graus):
    teta2rad = math.radians(teta2graus)
    senteta1rad = (n2*math.sin(teta2rad))/n1
    if senteta1rad > 1:
        return True 
    else: 
        return False
    
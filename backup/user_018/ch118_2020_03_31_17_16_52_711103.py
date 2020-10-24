import math

def reflexao_total_interna(n1,n2,teta2):
    teta2rad = math.radians(teta2)
    teta1rad = (n2*math.sin(teta2rad))/n1
    senteta1 = math.sin(teta1rad)
    if senteta1 > 1:
        return True 
    else: 
        return False
    
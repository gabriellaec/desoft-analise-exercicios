import math

def reflexao_total_interna(n1, n2, teta2):
    y = 180*math.asin(math.sin(n1*math.pi/180*n2))/math.pi
    if y > 1:
        return True
    else:
        return False

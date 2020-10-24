import math

def reflexao_total_interna(n1, n2, teta2):
    y = n1*math.sin(teta2*math.pi/180)/n2
    if y > 1:
        return True
    else:
        return False

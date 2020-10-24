import math

def reflexao_total_interna(n1, n2):
    y = math.sin(n1*math.pi/180*n2)
    if y > 1:
        return True
    else:
        return False

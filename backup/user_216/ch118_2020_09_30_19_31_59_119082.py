import math

def reflexao_total_interna(n1,n2,teta2):
    teta2 = math.radians(teta2)
    if math.sin(teta2) > n2/ n1:
        return True
    else:
        return False
import math

def reflexao_total_interna(n1,n2,teta2):
    O2 = math.radians(O2)
    if math.sin(O2) > n1/ n2:
        return True
    else:
        return False
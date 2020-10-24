import math 

def reflexao_total_interna(n1,n2,o2):
    o2 = math.radians(o2)
    if math.sin(o2) > n1/n2:
        return True
    else:
        return False
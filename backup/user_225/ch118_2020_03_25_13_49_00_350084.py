import math
def reflexao_total_interna(n1, n2, a2):
    a2 = math.radians(a2)
    sena1 = (n2*math.sin(a2))/n1
    if sena1 > 1:
        return True
    else:
        return False
  
    
import math
def reflexao_total_interna(n1,n2,theta2):
    x = n2 * math.sin(math.radians(theta2))/n1
    if x > 1:
        return True
        
    else :
        return False
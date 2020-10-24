import math
def reflexao_total_interna(n1,n2,θ2):
    x = (n2*math.sin(math.degrees(θ2)))/n1
    y = math.sin(math.degrees(x))
    if  y > θ2:
        return True
    else :
        return False
    print(reflexao_total_interna)
 

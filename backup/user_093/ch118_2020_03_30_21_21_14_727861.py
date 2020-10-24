import math
def reflexao_total_interna(n1,n2,x):
    x = math.radians(x)
    teta1 = (n2*math.sin(x))/n1
    if teta1 > 1:
        return True
    else:
        return False

    

    

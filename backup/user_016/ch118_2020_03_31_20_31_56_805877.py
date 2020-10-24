import math
def reflexao_total_interna(n1,n2,teta2):
    if n1>n2:
        return False
    else:
        teta2s = math.sin(math.radians(teta1))*n1/n2 
        teta2 = math.asin(teta2s)
        if math.sin(teta2) > 1:
            return True
        else:
            return False
    
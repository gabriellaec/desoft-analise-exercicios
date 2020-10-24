import math
def reflexao_total_interna(n1,n2,teta2):
    if n1>n2:
        return False
    else:
        teta1 = math.sin(math.radians(teta2))*n1/n2
        if teta1>1:
            return True
        else:
            return False
    
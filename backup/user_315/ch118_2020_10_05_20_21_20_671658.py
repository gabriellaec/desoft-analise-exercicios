import math
def reflexao_total_interna(n1,n2,teta2):
    x = math.sin(math.radians(teta2))
    teta1 =(n2*x)/n1
    if teta1 >= 1:
        return True
    else:
        return False
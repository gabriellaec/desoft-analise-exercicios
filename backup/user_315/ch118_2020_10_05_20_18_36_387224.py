import math
def reflexao_total_interna(n1,n2,teta2):
    x = math.sin(math.radians(teta2))
    z =(n1*x)/n2
    teta1 = math.asin(z)
    if teta1 >= 1:
        return True
    else:
        return False
import math
def reflexao_total_interna(n1,n2,teta1):
    seno = math.sin(math.radians(teta1))*n1/n2
    if (seno < 1):
        return False
    else:
        return True
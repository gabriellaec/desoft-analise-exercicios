import math
def reflexao_total_interna(n1,n2,teta2):
    seno = math.sin(math.radians(teta2))*n1/n2
    if (seno > 1):
        return True
    else:
        return False
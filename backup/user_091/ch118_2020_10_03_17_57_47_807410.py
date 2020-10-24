import math
def reflexao_total_interna(n1,n2,teta2):
    math.sin(math.radians(teta1))=n2*math.sin(math.radians(teta2))/n1
    if math.sin(math.radians(teta1)) > 1:
        return True
    else:
        return False
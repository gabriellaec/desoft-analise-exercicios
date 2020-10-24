import math
def reflexao_total_interna(n1,n2,teta2):
    sent1 = (math.sin(teta2))*n2/n1
    if sent1 > 1:
        return True
    if sent1 == 1:
        return False


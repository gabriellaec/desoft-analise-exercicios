import math
def reflexao_total_interna(n1,n2,teta2):
    teta2*=math.pi/180
    sent1 = (math.sin(teta2))*n2/n1
    if sent1 > 1:
        return True
    else:
        return False


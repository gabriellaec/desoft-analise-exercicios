import math


def reflexao_total_interna(n1,n2,teta2):
    teta2Rad=math.radians(teta2)
    senteta1=(n2/n1)*math.sin(teta2Rad)
    if n2>n1 and senteta1>1:
        return True
    else:
        return False
import math
def reflexao_total_interna(n1, n2, teta2):
    L=n1/n2
    teta1=math.sin(math.radians(L))
    if teta2>teta1:
        return True
    else: 
        return False
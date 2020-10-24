import math
def reflexao_total_interna(n1, n2, teta2):
    L=n2/n1
    x=math.sin(math.radians(L))
    teta1=math.asin(x)
    if teta2>teta1:
        return True
    else: 
        return False
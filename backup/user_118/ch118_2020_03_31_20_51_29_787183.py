import math
def reflexao_total_interna(n1,n2,teta2):
    L=n1/n2
    x=math.sin(math.radians(L))
    teta1=math.degrees(math.asin(x))
    teta2!=math.degrees(teta2)
    if teta2!>teta1:
        return True
    else:
        return False
    
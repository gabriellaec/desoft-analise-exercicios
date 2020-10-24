import math
def reflexao_total_interna(n1,n2,teta2):
    d1=n2/n1
    d2=math.sin(math.radians(teta2))
    d=math.sin(math.radians(teta1))
    d=d1*d2
    if(d>1):
        return True
    else:
        return False
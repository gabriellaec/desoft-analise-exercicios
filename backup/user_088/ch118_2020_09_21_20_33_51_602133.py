import math
def reflexao_total_interna(n1,n2,teta2):
    d1=n2/n1
    d2=math.sin(math.radians(teta2))
    teta1=math.asin(math.radians(d1*d2))
    d=math.sin(math.degrees(teta1))
    if(d>1):
        return True
    else:
        return False
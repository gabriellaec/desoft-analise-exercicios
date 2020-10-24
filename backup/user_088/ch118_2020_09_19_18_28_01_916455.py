import math
def reflexao_total_interna(n1,n2,teta2):
    x=(n2/n1)
    y=math.sin(math.radians(teta2))
    teta1=(math.degrees(math.asin(x*y)))
    if(math.sin(teta2)>1):
        return True
    else:
        return False
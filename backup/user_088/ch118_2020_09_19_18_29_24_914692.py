import math
def reflexao_total_interna(n1,n2,teta2):
    x=(n2/n1)
    y=math.sin(math.radians(teta2))
    math.sin(teta1)=(math.degrees(x*y))
    if(math.sin(teta1)>1):
        return True
    else:
        return False
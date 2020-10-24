import math
def reflexao_total_interna(n1,n2,teta2):
    d1=n2/n1
    d2=math.radians(math.sin(teta2))
    math.sin(teta1)=d1*d2
    if(math.degrees(math.radians(math.sin(teta1)>1))):
        return True
    else:
        return False
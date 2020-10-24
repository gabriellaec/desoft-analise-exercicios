import math
def reflexao_total_interna(n1,n2,teta2):
    if(n1>n2):
        x=math.radians(teta2)
        y=math.sin(x)
        if(y>1):
            return True
        else:
            return False

    else:
        return False
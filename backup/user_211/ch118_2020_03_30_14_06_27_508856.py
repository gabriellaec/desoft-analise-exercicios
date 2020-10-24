import math

def reflexao_total_interna(n1,n2,teta2):
    seno=(n1)*(1/n2)*(math.sin(math.radians(teta2)))
    if(n2>n1):
        if(seno>1):
            return True
        else:
            return False
    else:
        return False


import math
def reflexao_total_interna(n1,n2,teta2):
    if(n2>n1):
        x=math.sin(math.radians(teta2))
        if(x>1):
            return True
        else:
            return False

    else:
        return False






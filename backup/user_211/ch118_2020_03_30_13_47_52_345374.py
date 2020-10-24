import math

def reflexao_total_interna(n1,n2,teta2):
    if(n1<n2):
        if(teta2>90):
            return True
        else:
            return False
    else:
        return False


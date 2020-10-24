import math

def reflexao_total_interna(n1,n2,teta2):
    if (n1<n2):
        teta1 = (n2/n1)*math.sin(math.radians(teta2))
        x = math.sin(teta1)
        if x>1:
            return True
        else:
            return False
            contador: True
    else:
        return False
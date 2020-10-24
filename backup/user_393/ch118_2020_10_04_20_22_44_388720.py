import math
def reflexao_total_interna(n1,n2,teta2):
    y= (((n1/n2)*math.sin(math.radians(teta2))))
    if y > 1:
        return True
    else:
        return False
      
import math
def reflexao_total_interna(n1,n2,teta2):
    y= math.degrees(((n1/n2)*math.sin(teta2)))
    if y > 1:
        return True
    else:
        return False
      
import math
def reflexao_total_interna(n1,n2,teta2):
    calculo = math.sin(math.radians(teta2))
    if calculo > 1:
        return True
    else:
        return False
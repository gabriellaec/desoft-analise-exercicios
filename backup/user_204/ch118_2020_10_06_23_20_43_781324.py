import math
def reflexao_total_interna(n1,n2,teta2):
    teta1 = (n2 * math.sin(math.radians(teta2))) / n1
    calculo = math.sin(math.radians(teta1))
    if calculo > 1:
        return True
    else:
        return False
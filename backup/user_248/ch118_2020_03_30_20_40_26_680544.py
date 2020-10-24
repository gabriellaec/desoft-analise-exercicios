import math
aparece=True
def reflexao_total_interna(n1,n2,θ2):
    x=(n2/n1)*math.sin(math.radians(θ2))
    if x>1:
        aparece=True
    elif x<1:
        aparece=False
    return aparece
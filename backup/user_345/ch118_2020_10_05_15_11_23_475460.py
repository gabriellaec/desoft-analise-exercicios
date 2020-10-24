import math
def reflexao_total_interna(n1, n2, a1):
    seno1 = math.sin(math.radians(a1))
    seno2 = (n1/n2)*seno1
    if seno2 > 1:
        reflexao_interna_total= True
    else:
        reflexao_interna_total= False
    return reflexao_interna_total
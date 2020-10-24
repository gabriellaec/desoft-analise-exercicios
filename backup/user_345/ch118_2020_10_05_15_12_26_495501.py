import math
def reflexao_total_interna(n1, n2, teta2):
    seno2 = math.sin(math.radians(teta2))
    seno1 = (n2/n1)*seno2
    if seno1 > 1:
        reflexao_interna_total= True
    else:
        reflexao_interna_total= False
    return reflexao_interna_total
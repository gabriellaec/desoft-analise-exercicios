import math
def reflexao_total_interna(n1,n2,t2):
    limite = math.asin(math.radians(n2/n1))
    if t2>limite:
        reflexao_total = True
        return reflexao_total
    else:
        reflexao_total = False
        return reflexao_total

from math import*
def reflexao_total_interna(n1, n2, o2):
    X = (n2*sin(radians(o2)))/n1
    if X > 1:
        return True
    else:
        return False
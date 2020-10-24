import math
def reflexao_total_interna(n1, n2, a2):
    primeira_pt_equacao = n1/n2
    a2 = math.radians(a2)
    x = primeira_pt_equacao * (1/ math.sin(a2))
    a1 = math.sin(x)
    if a1 > 1:
        return True
    else:
        return False


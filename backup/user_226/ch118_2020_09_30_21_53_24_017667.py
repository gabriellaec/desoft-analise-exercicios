import math
def reflexao_total_interna(n1, n2, a2):
    a2 = math.radians(a2)
    if a2 == 0:
        return False
    else:
        resposta = n1/(n2 * math.sin(a2))
        if resposta > 1:
            return True
        else:
            return False




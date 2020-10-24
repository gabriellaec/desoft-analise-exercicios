import math
def reflexao_total_interna(n1, n2, angulo2):
    seno1 = n1 / n2 * math.sin(math.radians(angulo2))
    if seno1 > 1:
        return True
    else:
        return False
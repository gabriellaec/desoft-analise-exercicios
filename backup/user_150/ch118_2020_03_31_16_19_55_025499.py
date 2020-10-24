from math import *

def reflexao_total_interna(n1, n2, θ2):
    senθ1 = n2 * sin(radians(θ2)) / n1
    if senθ1 > 1:
        return True
    else:
        return False
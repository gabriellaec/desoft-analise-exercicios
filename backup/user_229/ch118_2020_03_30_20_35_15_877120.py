aparece = True
import math
def reflexao_total_interna(n1, n2, θ2):
    y = (math.sin(math.radians(θ2)))*(n2)/(n1)
    if y > 1:
        aparece = True
    elif y < 1:
        aparece = False
    return aparece
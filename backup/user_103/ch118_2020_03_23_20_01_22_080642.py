import math
def reflexao_total_interna(n1, n2, θ2):
    θ1=math.degrees(math.asin((n1*math.sin(math.radians(θ2))/n2)))
    if math.sin(θ1)>1:
        return "Verdadeiro"
    else:
        return "Falso'
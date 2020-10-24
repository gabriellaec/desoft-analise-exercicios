import math
def snell_descartes(n1,n2,θ1):
    θ1 = math.radians(θ1)
    sen_2 = (n1*math.sin(θ1))/n2
    θ2 = math.asin(sen_2)
    θ2 = math.degrees(θ2)
    return θ2
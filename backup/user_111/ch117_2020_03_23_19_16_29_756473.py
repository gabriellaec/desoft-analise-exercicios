import math
def snell_descartes(n1,n2,θ1):
    math.sin(θ2)=(n1*math.sin(θ1))/n2
    θ2=math.asin(θ2)
    return θ2
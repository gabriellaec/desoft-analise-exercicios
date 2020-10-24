import math
def snell_descartes(n1,n2,θ1):
    θ2=math.asin((math.sin(θ1)*n2)/n1)
    return θ2
def graus(θ2):
    graus=(θ2*180)/math.pi
    return graus
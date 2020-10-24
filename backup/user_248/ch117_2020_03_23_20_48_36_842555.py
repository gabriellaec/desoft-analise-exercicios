import math
def snell_descartes(n1,n2,θ1,θ2):
    math.sinθ2=n1*math.sinθ1/n2
    return θ2
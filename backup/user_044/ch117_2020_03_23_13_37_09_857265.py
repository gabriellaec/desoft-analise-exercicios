import math
def snell_descartes(n1,n2,θ1):
    y= math.degrees((math.asinh(θ1))*n1)/n2
    return y
    
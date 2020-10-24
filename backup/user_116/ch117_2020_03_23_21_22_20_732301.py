from math import sin
def snell_descartes(n1,n2,θ1):
    θ2=n1*(sin(θ1))/n2
    return sin(θ2)

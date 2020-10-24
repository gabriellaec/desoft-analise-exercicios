from math import*

def snell_descartes(n1, n2, θ1):
    a = (n1/n2)*sin(θ1)
    return asin(a)
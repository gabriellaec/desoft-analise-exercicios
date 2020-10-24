import math

def snell_descartes(n1, n2, θ1):
    a = (n1/n2)*math.sin(math.radians(θ1))
    return (math.degrees(math.asin(a)))
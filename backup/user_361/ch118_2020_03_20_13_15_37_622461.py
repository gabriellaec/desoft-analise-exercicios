import math

def reflexao_total_interna(n1, n2, θ1,):
    print(n1,n2,θ1,math.asin(n1*math.sin(math.radians(θ1))/n2))
    return (n1*math.sin(math.radians(θ1))/n2) > 1
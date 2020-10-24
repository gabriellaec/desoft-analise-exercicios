import math
def reflexao_total_interna(n1,n2,θ1):
    x=n1/n2*math.sin(math.radians(θ1))
    θ2=math.asin(x)
    if θ2>1:
        print ("Verdadeiro")
    else:
        print ("Falso")
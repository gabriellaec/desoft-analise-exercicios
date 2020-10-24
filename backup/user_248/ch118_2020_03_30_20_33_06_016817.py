import math
def reflexao_total_interna(n1,n2,θ2):
    x=n2/n1*math.sin(math.radians(θ2))
    θ1=math.asin(x)
    if θ1>1:
        print ("Verdadeiro")
    else:
        print ("Falso")
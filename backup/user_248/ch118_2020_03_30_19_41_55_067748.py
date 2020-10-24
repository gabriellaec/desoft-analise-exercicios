import math
def reflexao_total_interna(n1,n2,θ1):
    x=n1/n2*math.sin(math.radians(θ1))
    y=math.asin(x)
    θ2=math.degrees(y)
    if θ2>1:
        print ("Verdadeiro")
    else:
        print ("Falso")
import math
def reflexao_total_interna(n1,n2,θ2):
    x=n1/n2*math.sin(math.radians(θ1))
    y=math.asin(x)
    if y>1:
        print ("Verdadeiro")
    else:
        print ("Falso")
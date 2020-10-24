import math
def reflexao_total_interna(n1,n2,θ):
    x=math.sin(math.radians(θ))
    if x>1:
        print ("Verdadeiro")
    else:
        print ("Falso")
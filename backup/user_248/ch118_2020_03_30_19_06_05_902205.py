import math
def reflexao_total_interna(θ):
    x=math.sin(math.radians(θ))
    if x>1:
        print ("Verdadeiro")
    else:
        print ("Falso")
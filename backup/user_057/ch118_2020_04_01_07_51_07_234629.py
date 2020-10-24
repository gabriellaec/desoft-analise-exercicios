import math

def reflexao_total_interna(n1,n2,θ2):
    θ2=math.radians(θ2)
    Senoθ2=math.sin(θ2)
    Senoθ1=(n2*Senoθ2)/n1
    if -1> Senoθ1 >1:
        return "verdadeiro"
    else:
        return "falso"

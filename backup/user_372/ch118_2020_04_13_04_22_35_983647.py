import math
def reflexao_total_interna(n1,n2,θ2):
    θ1rad=(θ1*math.pi/180)
    θ2=math.asin(math.sin(θ1)*(n1/n2))
    y=θ1
    if y=>0 and y<90:
        reflexao_interna=False
    elif y==90:
        reflexao_interna=True
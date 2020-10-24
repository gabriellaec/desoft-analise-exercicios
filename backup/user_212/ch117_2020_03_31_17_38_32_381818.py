import math

def snell_descartes (n1, n2, θ1):
   
    sen1=math.sin(math.radians(θ1))
    θ2= (n1/n2)* (sen1)
    θ2=math.asin(θ2)
    return math.degrees(θ2)
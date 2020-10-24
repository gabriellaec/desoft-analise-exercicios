import math
def snell_descartes(n1,n2,θ1):
    x=n1*math.sin(math.radians(θ1))/n2
    y=math.sin(x)
    θ2=math.degrees(y)
    return θ2
 
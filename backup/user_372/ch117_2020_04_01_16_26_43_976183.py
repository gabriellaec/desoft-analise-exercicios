import math
def snell_descartes(n1,n2,θ1):
    θ1rad=θ1*(math.pi/180)
    θ2=math.asin(math.sin(θ1rad)*(n1/n2))
    y=θ2*180/math.pi
    return y


    

    
    

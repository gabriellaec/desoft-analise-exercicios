import math 

def snell_descartes(n1, n2, θ1):
   
    θ2 = math.asin((n1 * math.sin(math.radians(θ1))) / n2)
    graus = θ2 * (180/math.pi)
    return graus
    
    

    
    
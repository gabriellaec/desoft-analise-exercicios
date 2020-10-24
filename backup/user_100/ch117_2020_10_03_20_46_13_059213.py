import math 

def snell_descartes(n1, n2, θ1):
    θ2 = math.asin((n2 * math.sin(θ1)) / n1)
    graus = θ2 * (180/math.pi)
    return graus
    
    

    
    
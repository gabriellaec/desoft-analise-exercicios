import math
def snell_descartes(n1,n2,θ1):
    sen1=math.sin(math.radians(θ1))
    sen2=sen1*n1/n2
    θ2=math.asin(math.radians(sen2))
    return θ2
    
    
    
    
    
    
import math

def snell_descartes(n1,n2,theta1):
    X = math.sin(math.radians(theta1))
    Z = ((n1/n2)*X)
    W = math.asin(Z)
    i = math.degrees(W)    
    
    return(i)
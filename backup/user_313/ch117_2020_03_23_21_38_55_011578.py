import math

def snell_descartes(n1,n2,theta1):
    x = math.radians(theta1)
    return(math.radians(((n1*x)/n2)))

print(snell_descartes(10,5,10))
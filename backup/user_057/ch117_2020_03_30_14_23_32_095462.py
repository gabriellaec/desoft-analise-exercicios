import math

def snell_descartes(n1,n2,θ1):
    X=(math.sin(θ1))*(n1)/n2
    θ2=math.degrees(math.asin(X))
    return θ2 

print (snell_descartes)


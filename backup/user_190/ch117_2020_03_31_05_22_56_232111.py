import math 
def snell_descartes(n1, n2, o1):
    x=((math.sin(o1*(180/math.pi)))*n1)/n2
    o2=math.sin(x*(180/math.pi))
    return (o2)
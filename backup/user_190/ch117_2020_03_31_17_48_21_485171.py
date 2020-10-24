import math 
def snell_descartes(n1, n2, o1):
    x=((math.sin(o1*(math.pi/180)))*n1)/n2
    o2=math.sin(x*(math.pi/180))
    return (math.degrees(o2))
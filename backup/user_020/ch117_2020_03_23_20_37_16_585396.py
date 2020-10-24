import math
def snell_descartes(n1,n2,t1):
    z = (math.pi/180)*t1
    t2 = (n1*math.sin(z))/n2
    return t2
print(snell_descartes(10,20,30))
    
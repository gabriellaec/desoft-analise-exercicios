import math
def snell_descartes(n1,n2,t1):
    t1*=math.pi/180
    senot2 = n2/n1*(math.sin(t1))
    t2 = (math.asin(senot2))*(180/math.pi)
    return t2
    
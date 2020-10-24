import math
def  snell_descartes(n1,n2,o1):
    o1 = o1*(pi/180)
    x = (n1*math.sin(o1))/n2
    x = math.sin(x)
    o2 = math.asin(x)
    return(o2)
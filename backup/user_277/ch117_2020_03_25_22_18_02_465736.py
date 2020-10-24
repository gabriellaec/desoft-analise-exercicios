import math
def snell_descartes(n1,n2,o1):
 
    o2=((math.pi)*math.asin(n1*math.sin(o1)/n2))/180
    o2=math.degree(o2)  
    o1=math.degree(o1)
    return o2
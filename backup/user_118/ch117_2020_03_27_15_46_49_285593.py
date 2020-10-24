import math
def snell_descartes(n1,n2,t1):
    t2=(n1*t1)/n2
    return t2
m1=1
m2=2
a1=math.degrees(60)
a2=math.degrees((m1*a1)/m2)
print (snell_descartes(m1,m2,a1))

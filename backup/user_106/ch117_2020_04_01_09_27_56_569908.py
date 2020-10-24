import math

def snell_descartes(n1,n2,t1):
    t2r=math.radians(t2)
    t1r=math.radians(t1)
    (n1/n2)*math.sin(t1r)=math.sin(t2r)
    return (t2)
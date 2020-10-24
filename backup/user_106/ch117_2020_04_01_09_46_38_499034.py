import math

def snell_descartes(n1,n2,t1):
    t1r=math.radians(t1)
    st1r=math.sin(t1r)
    st2r=(n1/n2)*st1r
    t2r=math.asin(st2r)
    tr=math.degrees(t2r)
    return (t2)
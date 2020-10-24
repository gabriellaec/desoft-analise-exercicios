import math

def reflexao_total_interna(n1,n2,t2):
    t2r=math.radians(t2)
    st2r=math.sin(t2r)
    st1r=(n2/n1)*st2r
    t1r=math.asin(st1r)
    t1=math.degrees(t1r)
    n2>n1
    if st2r>1:
        return True
    if t1>t2:
        return False
import math

def reflexao_total_interna(n1,n2,t2):
    t2r=math.radians(t2)
    st1r=(n2/n1)*math.sin(t2r)
    if n2>n1 and st1r>1:
        return True
    else:
        return False
import math
def reflexao_total_interna(n1, n2, t2):
    t1=(math.sin(math.radians(t2))*n2)/n1
    if t1>1:
        return (True)
    else:
        return(False)
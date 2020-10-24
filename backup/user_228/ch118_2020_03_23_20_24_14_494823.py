import math
def reflexao_total_interna(n1,n2,s):
    a=n2*math.sin(math.radians(s))/n1
    y=math.degrees(a)
    if y>1:
        return(True)
    else:
        return(False)
    
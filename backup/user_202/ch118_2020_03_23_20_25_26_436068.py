import math
def reflexao_total_interna(n1,n2,o2):
    x = n2*math.sin(math.radians(o2))/n1
    x = math.asin(x)
    if x >= 0 and x < 90:
        return(False)
    else:
        return(True)
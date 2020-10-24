import math
def encontra_maximo(l):
    a = l[0]+l[1]+l[2]
    b =[max(a), math.fabs(min(a))]
    
    
    
    return(int(max(b)))
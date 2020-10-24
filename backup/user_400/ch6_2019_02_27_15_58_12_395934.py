import math
def encontra_maximo(l,m,n):
    a = l+m+n
    b =[max(a), math.fabs(min(a))]
    
    
    
    return int(max(b))

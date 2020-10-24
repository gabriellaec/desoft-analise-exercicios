import math
def reflexao_total_interna(n1,n2,o2):
    o2rad= o2*math.pi/180
    o1 =math.asin(math.sin(o2rad)*(n2/n1))
    y = o1 * 180 / math.pi
    return (y)
    
    if y>1:
        print('reflexao interna')
    else:
        print('refracao')
    
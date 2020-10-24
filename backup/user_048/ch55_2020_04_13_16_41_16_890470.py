import math
def encontra_maximo(ma):
    m=ma[0][0]
    for e in ma:
        for i in e:
            if i>m:
                m=i
            else:
                m=m
    return math.sqrt(m**2)    
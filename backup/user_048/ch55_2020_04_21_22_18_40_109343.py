import numpy as np
def encontra_maximo(ma):
    if len(ma)>0:
        av=np.absolute(ma)
        m=np.max(av)
    else:
        m=0
    return m
def encontra_maxima(mat):
    a=mat[0][0]
    for i in mat:
        for j in i:
            if j>a:
                a=j
            else:
                a=a
    return a
def  interseccao_valores (x,y):
    l=[]
    for kx,vx in x.items():
        for ky,vy in y.items():
            if vx==vy:
                l.append(vx)
    return l
 
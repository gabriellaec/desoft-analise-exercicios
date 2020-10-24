def segundos_entre(x,y):
    X = x.replace(':','')
    Y = y.replace(':','')
    hx = int(X[:2])*3600
    mx = int(X[2:4])*60    
    sx = int(X[4:])
    hy = int(Y[:2])*3600
    my = int(Y[2:4])*60
    sy = int(Y[4:])
    total = (hy-hx)+(my-mx)+(sy-sx)
    return total
    
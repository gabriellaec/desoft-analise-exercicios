def distancia_euclidiana (X1,Y1,X2,Y2):
    d=(X2-X1)**2
    a=(Y2-Y1)**2
    b=d-a
    f=b**(1/2)
    return f

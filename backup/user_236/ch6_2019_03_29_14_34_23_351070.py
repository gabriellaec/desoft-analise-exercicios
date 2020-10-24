def encontra_maximo(matriz):
    m=matriz[0][0]
    c1=0
    while c1<3:
        c2=0
        while c2<3:
            if matriz[c1][c2]>m:
                m=matriz[c1][c2]
            c2+=1
        c1+=1
    return(m)
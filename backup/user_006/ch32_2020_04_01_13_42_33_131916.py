def lista_primos(n):
    lista=[]*n
    g=0
    nalista=0
    v=False
    while nalista!=n:
        if g==0 or g==1:
            v= False
        else:
            if g==2:
                v= True
            else:
                if g%2==0:
                    v=False
                else:
                    i=1
                    while i<(g-1)/2:
                        if g%(g-2*i)==0:
                            v= False
                            i=(g-1)/2
                        else:
                            i=i+1
                        v=True
        if v==True:
            lista.append(g)
            nalista=nalista+1
        g=g+1
    return lista
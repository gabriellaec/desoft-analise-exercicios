def lista_primos(n):
    lista=[]*n
    g=0
    v=False
    while g<len(lista):
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
                        else:
                            i=i+1
                        v= True
        if True:
            lista.append(g)
        g=g+1
    return lista
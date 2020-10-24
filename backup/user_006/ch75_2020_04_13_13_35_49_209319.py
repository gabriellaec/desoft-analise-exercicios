def verifica_primos(lista):
    dicio={}
    g=0
    v=True
    while g<len(lista):
        numero=lista[g]
        if numero<0:
            numero2=numero*(-1)
            if numero2==0 or numero2==1:
                v= False
            else:
                if numero2==2:
                    v= True
                else:
                    if numero2%2==0:
                        v= False
                    else:
                        i=1
                        while i<(numero2-1)/2:
                            if numero2%(numero2-(2*i))==0:
                                v= False
                                i=(numero2-1)/2
                            else:
                                i=i+1
                        v= True
        if v==True:
            dicio[numero]=True
        else:
            dicio[numero]=False
        g=g+1	
def verifica_primos(lista):
    dic={}
    i=3
    for e in lista:
        if e<=1:
            dic[e]= False
        if e%2==0:
            if e==2:
                dic[e]=True
            else:
                dic[e]=False
        else:
            while i<e:
                if e%i==0:
                    dic[e]=False
                else:
                    i+=2
            dic[e]=True
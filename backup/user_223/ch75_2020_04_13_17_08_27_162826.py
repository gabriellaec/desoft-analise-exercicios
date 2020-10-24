def verifica_primos(lista):
    dic={}
    i=3
    for e in lista:
        el = int(e)
        if el<=1:
            dic[e]= False
        if el%2==0:
            if el==2:
                dic[e]=True
            else:
                dic[e]=False
        else:
            while i<el:
                if el%i==0:
                    dic[e]=False
                else:
                    i+=2
            dic[e]=True
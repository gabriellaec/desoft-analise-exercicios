def verifica_primos(lista):
    dic={}
    for i in lista:
        if i==-1 or i==0 or i==1:
            dic[i]=False
        elif i==2:
            dic[i]=True
        else:
            dic[i]=True
            if i%2=0:
                dic[i]=False
            else:
                d=3
                while i>d:
                    if i%d=0:
                        dic[i]=False
                        break
                    else:
                        d+=2
    return dic
                    
        
        
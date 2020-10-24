def lista_primos(n):
    s=[]
    o=[]
    i=0
    while len(s)<n:
        if i==0 or i==1:
            o.append(i)
            i+=1
        elif i==2:
            s.append(i)
            i+=1
        else:
            divisores=0
            for divisor in range(1,i):
                if i%divisor==0:
                    divisores+=1
            if divisores>1:
                o.append(i)
                i=1
            else:
                s.append(i)
                i+=1
    return(s)
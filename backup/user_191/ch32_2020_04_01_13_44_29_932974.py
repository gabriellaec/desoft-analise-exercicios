def lista_primos(n):
    s=[]
    o=[]
    while len(s)<n:
        if n==0 or n==1:
            o.append(n)
            n+=1
        else:
            divisores=0
            for divisor in range(1,n):
                if n%divisor==0:
                    divisores+=1
            if divisores>1:
                o.append(n)
                n+=1
            else:
                s.append(n)
                n+=1
    return(s)
def maior_primo_menor_que(n):
    if n==0 or n==1:
        return(-1)
    elif n==2:
        return(n)
    elif n<0:
        return(-1)
    else:
        divisor=0
        for divisores in range(1,n):
            if n%divisor==0:
                divisores+=1
        if divisores>1:
            n-=1
        else:
            return(n)
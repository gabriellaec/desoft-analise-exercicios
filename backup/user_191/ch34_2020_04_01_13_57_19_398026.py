def maior_primo_menor_que(n):
    i=n
    if i==0 or i==1:
        i-=1
    elif i==2:
        return(i)
    elif i<0:
        return(-1)
    else:
        divisor=0
        for divisores in range(1,i):
            if i%divisor==0:
                divisores+=1
        if divisores>1:
            i-=1
        else:
            return(i)
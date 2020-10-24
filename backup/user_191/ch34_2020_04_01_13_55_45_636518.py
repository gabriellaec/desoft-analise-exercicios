def maior_primo_menor_que(n):
    i=n-1
    if i==0 or i==1:
        i-=1
    elif i==2:
        return(i)
    else:
        divisor=0
        for divisores in range(1,i):
            if i%divisor==0:
                divisores+=1
        if divisores>1:
            i-=1
        else:
            return(i)
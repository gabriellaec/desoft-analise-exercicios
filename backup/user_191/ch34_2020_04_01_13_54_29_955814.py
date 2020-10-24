def maior_primor_menor_que(n):
    i=n-1
    divisor=0
    for divisores in range(1,i):
        if i%divisor==0:
            divisores+=1
    if divisores>1:
        i-=1
    else:
        return(i)
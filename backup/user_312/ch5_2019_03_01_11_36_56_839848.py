def maior_primo_menor_que(n):
    if n==1:
        return -1
    i=2
    i2=2
    primo=0
    max=0
    while i<=n:
        while i2<=i:
            if i%i2 == 0:
                primo+=1
            i2+=1
            #print(i,i2)
        if primo<2:
            max=i2
        primo=0
        i2=1
        i+=1
    return max
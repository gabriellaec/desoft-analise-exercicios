def maior_primo_menor_que(n):
    i=n
    while i>1:
        i-=1
        if n%i==0:
            return i
    i=2
    while i<n:
        if n%i!=0:
            return n
        else:
            return -1
        

        

        
def maior_primo_menor_que(n):
    while n>1:
    if n!=0 and n!=1:
        if n%2==0:
            i=n-1
        else:
            i=n-2
        while i>1:
            if n%i!=0 and n%2!=0:
                i-=2
            else:
                break 
        return (n)
    else:
        n-=1
   
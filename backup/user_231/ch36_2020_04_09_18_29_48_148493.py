def fatorial(n):
    if n==0:
        return n
    if n==1:
        return n
    i=n-1
    while i>=1:
        n= n*i
        i -=1
    return n
        

def fatorial(n):
    i=0
    a=1
    while i<n:
        n=n*(n-a)
        a=a+1
        i=i+1
    return n 
        
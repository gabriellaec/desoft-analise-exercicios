def teste(n):
    primo=True
    i=2
    if n<=1:
        primo=False
    while i<n:
        if n%i==0:
            primo=False
        i+=1
    return primo

def primos_entre(c,f):
    i=c
    l=[]
    while i=>c and i=<f:
        if teste(i):
            l.append(i)
        i+=1
    return l
     
            
    
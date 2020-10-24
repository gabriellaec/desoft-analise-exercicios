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

def primos_entre(a,b):
    while a<=b:
        if teste(a):
            c+=1
        a+=1
    return c    
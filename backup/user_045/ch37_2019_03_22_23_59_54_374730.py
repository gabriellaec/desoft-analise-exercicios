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

def imprime_primos(n):
    i=2
    c=0
    while c<=n:
        if teste(i):
            print(i)
            c+=1
        i+=1 
    
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
    while i<=n:
        if teste(i):
            print(i) 
        i+=1 
    
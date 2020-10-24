a=30

def imprime_primos(a):
    
    n=2
    while n<=a:
        i=2
        
        while i<n:
            if n%i==0:
                n-=1
        i+=1
            
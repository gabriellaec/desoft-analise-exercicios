n=int(input('valor de n'))
def fatorial(n):
    i=1
    p=1
    while i<=n:
        p*=i
        i+=1
    return p
print(fatorial(n))
        
    
    
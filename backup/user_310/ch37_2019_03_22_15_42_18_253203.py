def eh_primo(n):
    i=2
    if n==0 or n==1:
        return False
    while i<n:
        if n%i==0:
            return False
        i+=1
    return True

def imprime_primos(a):
    
    c=2
    i=0
    
    while i<a:
        if eh_primo(c):
            print (c)
            i+=1
        c+=1
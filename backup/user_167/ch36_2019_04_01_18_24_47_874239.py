def eh_primo(n):
    primo=true
    i=2
    if n<2:
        return false
    
    while i<n:
        if n%i==0:
            primo=false
        i+=1
    return primo
    
def eh primo(n):
    primo=True
    i=2
    if n<2:
        return False
    
    while i<n:
        if n%i==0:
            primo=False
            
        i+=1
    return primo
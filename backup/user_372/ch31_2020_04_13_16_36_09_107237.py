def eh_primo(n):
    i=1    
    while i<=n:
        i+=2
        if n%2!=0 and n%i!=0:
            primo=True 
        else:
            primo=False
        return primo
        
def eh_primo(x):
    c=True
    i=1
    if x==0 or x==1:
        return False
    if x==2:
        return True
    while i<x:
        if x%i==0 or x%2==0:
            c=False
            i+=2
        else:
            c=True
            i+=2
    return c
        
        
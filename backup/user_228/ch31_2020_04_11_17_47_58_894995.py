def eh_primo(x):
    i=1
    if x==0 or x==1:
        return False
    while i<x:
        if x%i==0 and x%2==0:
                return False
                i+=2
        else:
            return True
            i+=2
    
        
        
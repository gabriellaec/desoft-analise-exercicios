def eh_primo(x):
    i=1
    while i<x:
        if x%i==0:
            if x%2==0:
                return False
                i+=2
        else:
            return True
            i+=2
        
        
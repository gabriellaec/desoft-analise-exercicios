def eh_primo(x):
    if x==0 or x==1: 
        return False
    elif x==2:
        return True
    else:
        i = 1
        while i<x:
            w = x%i
            if w!=0:
                return True  
            else:
                return False
            i+=2


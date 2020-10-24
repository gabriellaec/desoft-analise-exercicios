def eh_primo(x):
    if x==0 or x==1: 
        return False
    elif x==2:
        return True
    else:
        i = 1
        while i<x:
            y = x%2
            w = x%i
            i+=2
            if y!=0 or w!=0:
                return True  
            else:
                return False
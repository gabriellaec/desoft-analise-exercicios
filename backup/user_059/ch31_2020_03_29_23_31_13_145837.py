def eh_primo(x):
    i = 3
    if x==0 or x==1: 
        return False
    elif x==2:
        return True
    else:
        while i<x:
            y = x%2
            w = x%i
            i+=2
            if y==0 or w ==0:
                return False  
            else:
                return True
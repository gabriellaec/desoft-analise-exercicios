def eh_primo(x):
    z=3
    if x<2:
        return False
    if x==2:
        return True
    elif x%2==0: 
        return False
    else:
        while z<x-2:
            if x%(z)==0:
                return False
                
            z+=2
        return True
def eh_primo(x): 
    if (x==2):
        return True
    elif (x==1):
        return False
    elif (x%2==0):
        return False
    divisores = 0
    while (divisores<x):
        divisores = divisores + 1
        if (x%divisores==0 and divisores!=1):
            return False
        else:
            return True
    else:
        return True
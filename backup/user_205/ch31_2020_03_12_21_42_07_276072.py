def eh_primo(x): 
    if (x==2):
        return True
    elif (x%2==0):
        return False
    divisores = 1
    while (divisores<x):
        divisores = divisores + 2
        if (x%divisores==0):
            return False
        else:
            return True
    else:
        return False
    
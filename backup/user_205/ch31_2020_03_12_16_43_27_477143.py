def eh_primo(x): 
    if (x%2==0 and x!=2 or x!=0 or x!=1):
        return False
        divisores = 3
        while divisores<x:
            divisores = divisores + 2
            y = x%divisores==0
            return False
    else:
        return True
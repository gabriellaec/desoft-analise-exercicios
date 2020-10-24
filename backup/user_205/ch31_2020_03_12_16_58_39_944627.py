def eh_primo(x): 
    if (x%2==0):
        return False
    elif (x==2):
        return True
    elif (x==1 or x==0):
        return False
    divisores = 0
    while divisores<x and divisores !=0 and divisores!= 1 and divisores!=2:
        divisores = divisores + 2
        y = x%divisores==0
        return False
    else:
        return True
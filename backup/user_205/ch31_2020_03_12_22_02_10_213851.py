def eh_primo(x):
    if (x==2):
        return True 
    elif (x%2==0):
        return False
    divisor = 0
    while (divisor<x):
        divisor +=1
        if (x%(divisor%2!=0)==0):
            return True
        else:
            return False
    else:
        return False
        return True
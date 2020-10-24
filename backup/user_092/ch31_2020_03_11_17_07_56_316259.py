def eh_primo(x):
    if x<2:
        return False
    elif x == 2:
        return True
    else:
        t = 2
        while(t<x):
            if (x%t==0):
                return False
            else:
                return True
            t +=1
        
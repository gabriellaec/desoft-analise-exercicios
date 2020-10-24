def eh_primo(x):
    if x<2:
        return False
    else:
        t = 2
        while(t<x):
            if (x%t==0):
                return False
            elif t==0:
                return True
            else:
                return True
            t +=1
        
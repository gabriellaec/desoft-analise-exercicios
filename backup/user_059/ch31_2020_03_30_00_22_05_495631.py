def eh_primo(x):
    j = 0
    i = 0
    if x==0 or x==1:
        return False
    elif x==2:
        return True
    else:
        while i<=x or j<2:
            i+=1
            w=x%i
            if x==0:
                j+=1
                if j<=2:
                    return True
                else:
                    return False
            else:
                return False
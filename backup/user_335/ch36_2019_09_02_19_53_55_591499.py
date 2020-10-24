def eh_primo(x):
    if x==0:
        return False
    elif x==1:
        return False
    elif x==2:
        return True
    else:
        d = 3
        while d<=x:
            if x%2 == 0:
                return False
            else:
                if x==d:
                    return True
                if x%d == 0:
                    return False
                else:
                    d = d+2  
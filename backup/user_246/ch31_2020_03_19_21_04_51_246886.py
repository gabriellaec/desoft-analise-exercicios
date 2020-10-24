def eh_primo(x):
    if x==2:
        return True
    elif x==1:
        return False
    elif x%2==0:
        return False
    else:
        y=3
        while x%y!=0 and y!=x:
            y=y+2
            return True
    return False
        
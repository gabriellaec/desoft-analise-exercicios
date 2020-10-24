def eh_primo(x):
    if x==3:
        return True
    elif x==2:
        return True
    elif x==1 and x==25:
        return False
    elif x%2==0:
        return False
    else:
        y=3
        while not x%y==0:
            y=y+2
            return True
    return False


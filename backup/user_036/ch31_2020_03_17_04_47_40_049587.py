def eh_primo(x):
    if x==0:
        return(False)
    if x%2 != 0:
        return(True)
    elif x%3 != 0:
        return(True)
    elif x%5 != 0:
        return(True)
    elif x%7 != 0:
        return(True)
    elif x%9 != 0:
        return(True)
    elif x%11 != 0:
        return(True)
    else:
        return(False)
        
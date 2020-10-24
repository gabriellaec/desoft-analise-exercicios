def eh_primo(x):
    i = 3
    if x <= 1:
        return False
    if x%2==0:
        if x == 2:
            return True
        else:
            return False
    else:
        while i<x:
            if x%i==0:
                return False
            else:
                i+=2
    return True
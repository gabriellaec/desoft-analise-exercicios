def eh_primo(x):
    if x == 2:
        return False
    elif x == 0 or x == 1:
        return False
    else:
        i = 3
        while i < x:
            if x%i == 0:
                return False
            i = i+2
            else:
                return True
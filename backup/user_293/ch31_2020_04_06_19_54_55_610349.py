def eh_primo(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for e in range(2,x):
            a = x%e
            if a == 0:
                return False
        else:
            return True
       
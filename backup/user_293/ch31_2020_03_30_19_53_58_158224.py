def eh_primo(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        i = 2
        while i < x:
            a = x%i
            if a == 0:
                return False
            i += 1
        else:
            return True
       
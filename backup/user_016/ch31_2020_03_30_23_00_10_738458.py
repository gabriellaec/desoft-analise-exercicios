def eh_primo(x):
    r = x%2
    i = 3
    d = x % i
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        if r == 0:
            return False
        else:
            if x == i:
                return True
            while i < x:
                if d == 0:
                    return False
                i = i + 2
                if x == i :
                    return True
                else:
                    return False
        
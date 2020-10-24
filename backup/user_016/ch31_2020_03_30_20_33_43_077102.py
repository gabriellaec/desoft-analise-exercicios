def eh_primo(x):
    r = x%2
    i = 3
    d = x%i
    while x > 2:
        if r == 0:
            return False
        else:
            while i != 3:
                if d == 0:
                    return False
                else:
                    return True
                i = i + 2
    if x == 2:
        return True
    else:
        return False
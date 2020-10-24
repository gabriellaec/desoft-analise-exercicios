def eh_primo(x):
    r = x%2
    i = 3
    while x > 2:
        if r == 0:
            return False
        else:
            d = x%i
            i = i + 2
            if i < x and d == 0:
                return False
            else:
                return True
    if x == 2:
        return True
    else:
        return False
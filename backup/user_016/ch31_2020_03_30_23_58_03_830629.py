def eh_primo(x):
    r = x%2
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        if r == 0:
            return False
        else:
            i = 3
            d = x%i
            while i < x:
                if d == 0:
                    break
                i += 1
            if i == x:
                return True
            else:
                return False
            
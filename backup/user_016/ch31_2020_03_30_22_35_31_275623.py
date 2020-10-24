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
            if x == 3 and d == 0:
                return True
            elif x !=3 and d == 0:
                return False
            elif i >= 3:
                return True
            else:
                while i < x:
                    if d == 0:
                        break
                    i = i + 2
                return False
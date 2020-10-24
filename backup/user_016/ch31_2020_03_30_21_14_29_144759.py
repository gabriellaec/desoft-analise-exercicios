def eh_primo(x):
    r = x%2
    i = 3
    while x > 2:
        if r == 0:
            return False
        else:
            d = x%i
            if d == 0 and x != 3:
                return False
            elif d == 0 and x == 3:
                return True
            else:
                exercicio = True
                while exercicio:
                    if i < x:
                        i = i + 2
                        return True
                    else:
                        return False
    if x == 2:
        return True
    else:
        return False
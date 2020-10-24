def eh_primo(x):
    r = x%2
    d = x%1
    i = 3
    while x > 2:
        if r == 0:
            return False
        else:
            exercicio = True
            while exercicio:
                i = i + 2
                if d == 0:
                    return False
                else:
                    return True
    if x == 2:
        return True
    else:
        return False

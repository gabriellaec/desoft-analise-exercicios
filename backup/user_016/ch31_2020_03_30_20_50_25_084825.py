def eh_primo(x):
    r = x%2
    i = 3
    
    while x > 2:
        if r == 0:
            return False
        else:
            exercicio = True
            while exercicio:
                d = x%i
                if d != 0:
                    i = i+2
                    return True
                elif x == 3 and d == 0:
                    return True
                elif x !=3 and d==0:
                    return False
    if x == 2:
        return True
    else:
        return False
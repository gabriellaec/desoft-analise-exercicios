def eh_primo(x):
    r = x%2
    exercicio = True
    i = 3
    while exercicio:
        if r == 0:
            return False
        else:
            d = x%i
            i = i + 2
            if i < x and d == 0:
                return False
            else:
                return True

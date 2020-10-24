def eh_primo(n):
    if n<2:
        return False
    elif n==2:
        return True
    else:
        for r in range(2, n):
            if n%r == 0:
                return True
            else:
                return False
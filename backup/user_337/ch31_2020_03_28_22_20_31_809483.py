def eh_primo(n):
    if n == 1:
        return False
    elif n == 0:
        return False
    elif n == 2:
        return True
    else:
        if n%2 == 0:
            return False
        elif n%2 != 0:
            impar = []
            i = 0
            n = impar[i]
            if n%impar[i] == 0:
                i = i + 1
                return False
            else:
                return True
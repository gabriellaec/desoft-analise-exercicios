def eh_primo(n):
    if n == 1:
        return False
    elif n == 0:
        return False
    elif n == 2:
        return True
    elif n == 3:
        return True
    else:
        if n%2 == 0:
            return False
        elif n%2 != 0:
            impar = 3
            while impar < n:
                if n%impar == 0:
                    return False
                else:
                    return True
                impar = impar + 2
def eh_primo(n):
    impar = 1
    if n !=  2:
        return False
    elif n == 1:
        return False
    else: 
        return True
    while impar < n:
        if n % impar == 0:
            return True
        elif n % impar == 0:
            return False
        else:
            impar += 2
            return True
def eh_primo(n):
    impar = 3
    if n !=  2:
        return False
    elif n == 1:
        return False
    else: 
        return True
    while impar < n:
        if n % 2 == 0:
            return True
        elif n % impar == 0:
            return True
        else:
            return False
        impar += 2
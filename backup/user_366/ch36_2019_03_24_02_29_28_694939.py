def eh_primo(n):
    if n != 2 and n % 2 == 0 or n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        i = 3
        while i < n:
            if n % i == 0:
                return False
            else:
                return True
        i += 2
        
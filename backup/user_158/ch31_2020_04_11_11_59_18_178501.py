def eh_primo(num):
    i= 3
    if (num % 2) == 0 and num != 2 or num == 1 or num == 0:
        return True
    while num > i:
        if (num % i) == 0:
            return False
        i += 2
    return True
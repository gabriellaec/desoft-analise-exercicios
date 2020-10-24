def eh_primo(num):
    i=2
    if num == 2:
        return True

    while i < num:
        if num % i == 0:
            return False
        i=i+1
    return True
def eh_primo(n):
    while n % 2 == 0:
        return False
    if n % 2 != 0 and n == 2:
        return False
    if n % 2 != 0:
        return True
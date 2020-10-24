def eh_primo(n):
    for e in range(2,n):
        if n % e == 0:
            return False
        else:
            return True
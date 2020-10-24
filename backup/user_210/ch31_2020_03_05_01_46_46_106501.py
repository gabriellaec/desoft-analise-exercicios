def eh_primo(n):
    if n == 0 or n==1:
        return False
    for c in range(2, n, 2):
        if n%c==0:
            return False
    return True
def número_primo(n):
    i = 2
    while i<n:
        if n%i == 0:
            return False
    return True

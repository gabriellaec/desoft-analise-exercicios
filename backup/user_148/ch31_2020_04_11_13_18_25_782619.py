def eh_primo(p):
    for c in range(1, p+1):
        if p % c == 0:
            return True
        else: return False
def eh_primo(p):
    i = 1
    
    while i<p:
        if p % i == 0:
            return False
        i += 2
    if p % 2 == 0:
        return False
    elif p == 2:
        return True
    else:
        return True
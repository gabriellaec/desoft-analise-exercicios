def eh_primo(p):
    tot = 0
    for c in range(1, p+1):
        if p % c == 0:
            return True
            tot+=1
        else:
            return False
    tot == 2

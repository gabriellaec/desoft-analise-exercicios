def eh_primo(p):
    tot = 0
    for c in range(1, p+1):
        if p % c == 0:
            tot+=1
            if tot == 2:
                return True
            else:
                return False
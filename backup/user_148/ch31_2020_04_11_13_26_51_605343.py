def eh_primo(p):
    tot = 0
    cont = []
    cont[0] = 1
    i = 1
    while p <= len(cont):
        if p % cont[i] == 0:
            i+=1
            if tot==2:
                tot+=1
                return True
        else:
            return False

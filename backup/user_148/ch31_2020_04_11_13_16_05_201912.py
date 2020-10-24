def eh_primo(p):
    cont = []
    cont[0] = 1
    i = 0
    while p<=cont:
        if p % cont[i] == 0:
            i+=1            
            return True
        else:
            return False
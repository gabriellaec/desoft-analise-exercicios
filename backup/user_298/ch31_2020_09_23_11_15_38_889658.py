def eh_primo(num):
    nao_primo = True
    t = 2
    while nao_primo:
        if num % t != 0:
            t += 1
            while nao_primo:
                if num % t != 0:
                    t += 2
                else:
                    nao_primo = False
        else:
            return False
    if nao_primo == False:
        return True
    else:
        return False    
print(eh_primo(num))
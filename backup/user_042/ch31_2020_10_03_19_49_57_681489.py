def eh_primo(p):
    if p % 2 != 0: 
        return 'True'
    else:
        i = 1
        while i < 10:
            i += 2
            if p % i == 0:
                return 'False'
            else:
                return 'True'     
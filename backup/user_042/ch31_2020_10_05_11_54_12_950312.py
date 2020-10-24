def eh_primo(p):
        if p == 0:
            return 'False'
        if p == 1:
            return 'False'
        if p % 2 == 0:
            return 'False'
        impares = 3
        while impares <= p:
            if p % impares == 0:
                return 'False'
            else: 
                return 'True'
            impares += 2
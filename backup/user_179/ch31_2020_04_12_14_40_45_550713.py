def eh_primo(numero):
    if numero == 2:
        return True
    else:
        i = 3
        while i <= numero:
            if numero/i == 1 :
                return True
            else: 
                i = i + 2
        return False
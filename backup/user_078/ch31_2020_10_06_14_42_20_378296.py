def eh_primo(numero):
    i = 3
    verific = False
    if numero%2 == 0:
        return False

    elif numero == 0 or numero == 1:
        return False

    elif numero == 2:
        return True

    else:

        while i < numero: #talvez o erro esteja aqui

            if numero%i == 0:
                verific = False
                i+=2
            
            else:
                verific = True
                i+=2
        
        return verific
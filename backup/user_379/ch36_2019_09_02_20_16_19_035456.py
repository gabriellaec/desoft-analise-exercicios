def eh_primo(numero):
    if numero<2:
        return False
    elif numero==2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        n = 3
        while n <= numero:
            if numero%n!=0:
                n+=1
                return True
            else:
                return False
            
def eh_primo(numero):
    if numero==0:
        return False
    elif numero==1:
        return False
    elif numero==2:
        return True
    elif numero==3:
        return True
    elif numero % 2==0 :
        return False
    else:
        i=3
        while i <= numero:
            if numero % i==0:
                return False
                break
            else:
                return True
                break
        i+=2
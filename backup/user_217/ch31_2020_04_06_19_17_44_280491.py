def eh_primo(numero):

    if numero%2 == 0: 
        return True

    else:
        i=3
        while i <=9:
            if numero%i == 0:
                return True

            else: 
                return False
            i+=2


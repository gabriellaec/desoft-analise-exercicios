def eh_primo(numero):
    divisor = 1
    while numero!=divisor and numero>divisor:
        divisor += 1
        if numero%divisor==0:
            return False
        elif numero==0 or numero==1:
            return False
        else:
            return True

def eh_primo(numero):
    divisor = 1
    while numero!=divisor and numero>divisor:
        divisor += 1
        if numero%divisor==0:
            return False
        else:
            return True

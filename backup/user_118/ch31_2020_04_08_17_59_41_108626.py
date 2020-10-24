def eh_primo(numero, divisor):
    x=numero/divisor
    divisor = 1
    while numero!=divisor and numero>divisor and x!=0:
        divisor += 1
        if numero%divisor==0:
            return False
        else:
            return True
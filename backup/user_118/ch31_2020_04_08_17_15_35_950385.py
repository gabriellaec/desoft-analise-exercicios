def eh_primo(numero, divisor):
    divisores = 0
    while numero>divisor>1:
        if (numero/divisor) == 0:
            divisores += 1
            if divisores > 1:    
                return False
            else:
                return True
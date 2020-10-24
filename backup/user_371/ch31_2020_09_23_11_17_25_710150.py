def  eh_primo(numero):
    i = 1
    if numero == 0 or numero == 1:
        return False
    if numero == 2:
        return True
    while i <= numero:
        i = i+2
        resto = numero % i 
        if resto == 0 and i != numero or numero % 2 == 0:
            return False
        elif i == numero :
            return True
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

def maior_primo_menor_que(numero):
    while numero > 2:
        if eh_primo(numero):
            return numero
        elif numero < 2:
            return -1
        else:
            numero-=1
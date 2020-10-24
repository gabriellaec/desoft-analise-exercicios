def eh_primo(numero):
    if numero < 2:
        return False
    contador = 2
    while contador < numero:
        if numero % contador == 0:
            return False
        contador += 1
    return True

def maior_primo_menor_que(numero):
    if numero > 1:
        while not eh_primo(numero):
            numero -= 1
        return numero
    else:
        return -1
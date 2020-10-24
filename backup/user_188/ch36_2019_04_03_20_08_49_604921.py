def eh_primo(numero):
    contador = 2
    while contador < numero:
        if numero % contador == 0:
            return False
        contador += 1
    return True
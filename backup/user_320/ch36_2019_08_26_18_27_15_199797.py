def eh_primo(numero):
    div = 0
    cont = 0
    while True:
        div += 1
        if int(numero) % div == 0:
            cont += 1
        if div == numero:
            break
    if cont > 2:
        return False
    return True
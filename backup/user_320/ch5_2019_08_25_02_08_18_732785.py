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


def maior_primo_menor_que(n):
    if (float(n)) <= 1:
        return -1
    if eh_primo(float(n)):
        return n
    num = n
    while not eh_primo(num):
        num -= 1
    return num

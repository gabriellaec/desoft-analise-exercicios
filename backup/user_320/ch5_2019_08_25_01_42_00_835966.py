def eh_primo(numero):
    if numero <= 0:
        return -1
    div = 0
    cont = 0
    while True:
        div += 1
        if numero % div == 0:
            cont += 1
        if div == numero:
            break
    if cont > 2:
        return False
    return True


def maior_primo_menor_que(n):
    if eh_primo(n):
        return f'{n}'
    num = n
    while not eh_primo(num):
        num -= 1
    return num
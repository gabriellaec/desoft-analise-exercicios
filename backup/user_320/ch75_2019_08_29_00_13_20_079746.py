def eh_primo(numero):

    div = 0
    cont = 0
    if numero <= 1:
        return False
    while True:
        div += 1
        if numero % div == 0:
            cont += 1
        if div == numero:
            break
    if cont > 2:
        return False
    return True


def verifica_primos(lista):
    dic = {valor: eh_primo(valor) for valor in lista}
    return dic
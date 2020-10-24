def eh_primo (numero):
    if numero == 1 or numero == 0:
        return False
    elif numero == 2:
        return True
    else:
        div = 2
        cont = 0
        while div < numero:
            if numero % div == 0:
                cont += 1
            div += 1
        if cont == 0:
            return True
        else:
            return False
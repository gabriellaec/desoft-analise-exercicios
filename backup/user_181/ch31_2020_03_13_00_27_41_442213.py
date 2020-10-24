def eh_primo(numero):
    cont = 0
    for i in range(2, (round(numero**.50) + 1)):
        if(numero % i == 0):
            cont = cont + 1
            break
    if (cont == 0 and numero != 1 and numero != 0):
        return True
    else:
        return False
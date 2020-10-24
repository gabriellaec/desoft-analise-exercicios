def quantos_uns(numero):
    numero_string = str(numero)
    qntd_uns = 0
    for i in range(0,len(numero_string)):
        if numero_string[i] == '1':
            qntd_uns += 1
    return qntd_uns
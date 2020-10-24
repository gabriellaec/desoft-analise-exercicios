def quantos_uns(numero):
    cont=0
    frequencia=0
    while cont<len(numero):
        if numero[cont] == 1:
            frequencia+=1
        cont+=1
    return frequencia
def quantos_uns(numero):
    total = 0
    numero = str(numero)
    for i in numero:
        if i == '1':
            total+=1
    return total
def quantos_uns(num):
    lista = list(str(num))
    if '1' in lista:
        x = lista.count('1')
    else:
        x = 0
    return x
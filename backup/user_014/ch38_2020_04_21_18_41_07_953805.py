def quantos_uns(numero):
    n = 0
    while n < len(numero):
        if numero[n] == '1':
            n += 1
        else:
            return n
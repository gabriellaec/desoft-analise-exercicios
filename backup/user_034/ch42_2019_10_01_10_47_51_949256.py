def quantos_uns(x):
    numero = str(x)
    total = 0
    for e in numero:
        if e == '1':
            total += 1
        else:
            total += 0
    return total
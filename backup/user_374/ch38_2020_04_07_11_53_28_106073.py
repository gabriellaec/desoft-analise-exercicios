def quantos_uns(a):
    show = str(a)
    quant = 0
    for i in show:
        if i == '1':
            quant += 1
    return quant

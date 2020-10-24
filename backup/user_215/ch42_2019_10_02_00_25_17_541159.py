def quantos_uns(n):
    qnt = 0
    for i in n:
        if i == 1:
            qnt += 1
            i += 1
        else:
            i += 1
            
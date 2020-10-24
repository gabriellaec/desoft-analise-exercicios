def quantos_uns(n):
    num = str(n)
    qnt = 0
    for u in num:
        if u == str(1):
            qnt += 1
    return qnt
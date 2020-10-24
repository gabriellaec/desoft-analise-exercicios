def quantos_uns(n):
    total = 0
    n = str(n)
    for i in n:
        if i == '1':
            total += 1
    return total
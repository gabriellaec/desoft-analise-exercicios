def quantos_uns(n):
    uns = []
    while (n > 0):
        if (n % 10 == 1):
            uns.append(1)
        n = int(n/10)
    return sum(uns) 
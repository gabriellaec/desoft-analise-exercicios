def quantos_uns(num):
    i = 0
    times = 0
    x = str(num)
    size = len(x)
    while i < size:
        if x[i] == 1:
            times += 1
        i += 1
    return times
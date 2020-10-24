def quantos_uns(num):
    i = 0
    times = 0
    size = len(num)
    while i<size:
        if num[i] == "1":
            times += 1
        i += 1
    return times
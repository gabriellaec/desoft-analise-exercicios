def calcula_media(l):
    d = 0
    sum = 0
    for i in l:
        for v in i.values():
            sum += v
            i += 1
    return sum/i
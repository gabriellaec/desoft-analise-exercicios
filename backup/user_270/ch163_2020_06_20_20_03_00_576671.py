def calcula_media(l):
    d = 0
    sum = 0
    for k in l:
        for v in k.values():
            sum += v
            d += 1
    return sum/d
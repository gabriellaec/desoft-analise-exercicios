def quantos_uns(n):
    algarismos1 = 0
    i = 0
    while i > 0:
        if n[i] == 1:
            algarismos1 += 1
            i += 1
        else:
            i += 1
            continue
    return algarismos1
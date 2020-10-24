def quantos_uns(n):
    m = str(n)
    algarismos1 = 0
    i = 0
    while i < len(m):
        if m[i] == 1:
            algarismos1 += 1
            i += 1
        else:
            i += 1
            continue
    return algarismos1
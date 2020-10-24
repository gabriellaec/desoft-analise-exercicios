def quantos_uns(n):
    n = str(n)
    i = 0
    c = 0
    while i<len(n):
        if n[i] == "1":
            c += 1
            i += 1
        else:
            i += 1
    return c
            
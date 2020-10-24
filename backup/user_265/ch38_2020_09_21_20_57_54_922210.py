def quantos_uns(a):
    p = str(a)
    i = 0
    Uns = 0
    while i < len(p):
        if p[i] == "1":
            i += 1
            Uns += 1
        else: 
            i += 1
    return Uns
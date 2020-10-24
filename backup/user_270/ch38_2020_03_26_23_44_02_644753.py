def quantos_uns(n):
    k = 0
    t = 0
    while k < len(n) :
        if n[k] == 1 :
            t += 1
        k += 1
    return t
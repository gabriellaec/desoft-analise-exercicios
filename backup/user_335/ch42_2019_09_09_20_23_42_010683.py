def quantos_uns(n):
    i = 0
    qn1 = 0
    n = str(n)
    while i < len(n):
        if n[i]== str(1):
            qn1 += 1
            i += 1
        else:
            i += 1
    return qn1
            
def quantos_uns(n):
    n = str(n)
    print(n)
    i = 0
    m = 0
    while i < len(n):
        if n[i] == str(1):
            m += 1
            i+= 1
        else:
            i += 1
    return m
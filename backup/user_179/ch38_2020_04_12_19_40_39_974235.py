def quantos_uns(n):
    i = 0
    uns = 0
    ns = str(n)
    while i < len(ns):
        if ns[i] == '1':
            uns = uns + 1
            i = i + 1
        else:
            i = i + 1
    return uns
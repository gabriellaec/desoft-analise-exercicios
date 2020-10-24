def quantos_uns (n):
    i = 0
    while i < len(n):
        if n[1] == 1:
            uns = uns + 1
            i = i + 1
        else:
            i = i + 1
    return uns
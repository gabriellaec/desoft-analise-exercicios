def conta_a(palavra):
    c = 0
    i = 0
    while i < len(palavra):
        if palavra[i] == 'a':
            c += 1
        i += 1
        return c
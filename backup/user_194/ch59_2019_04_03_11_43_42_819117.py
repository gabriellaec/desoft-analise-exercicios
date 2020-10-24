def conta_a(palavra):
    S = 0
    i = 0
    while i < len(palavra):
        if palavra[i] == 'a':
            S += 1
        i += 1
        return S
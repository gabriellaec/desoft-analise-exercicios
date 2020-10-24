def PiWallis(n):
    termo = [0]*n
    termo[0] = 2
    produtorio = 1
    i = 1
    while i < n:
        if i % 2 == 0:
            termo[i] = (i + 2)/(i + 1)
        else:
            termo[i] = (i + 1)/(i + 2)
        i += 1
    for x in termo:
        produtorio *= x
    return 2*produtorio
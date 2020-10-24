def conta_a(x):
    x = str(input( 'digita palavra: '))
    i = 0
    n = 0
    while i < len(x):
        if x[i] == 'a':
            n += 1
        i += 1
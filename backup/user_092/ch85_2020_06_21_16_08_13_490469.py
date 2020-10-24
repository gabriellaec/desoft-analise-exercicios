with open('macacos-me-mordam.txt', 'r') as arquivo:
    cc = arquivo.read()
    L = cc.split()
    i = 0
    for e in L:
        if e == 'Banana':
            i += 1
        elif e == 'BANANA':
            i += 1
        elif e == 'BaNaNa':
            i += 1
        elif e == 'banana':
            i += 1
    print(i)
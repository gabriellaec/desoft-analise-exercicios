with open(macacos-me-mordam.txt, 'r') as arquivo:
    i = 0
    for linha in arquivo:
        for palavra in linha:
            if palavra == 'banana':
                i += 1
    print(i)
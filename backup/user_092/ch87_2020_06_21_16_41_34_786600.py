with open('churras.txt''r') as arquivo:
    cc = arquivo.read()
    L = cc.split(',')
    i = 2
    while i <= L:
        n = float(L[i])
        valor += n
        i += 3
    print(valor)
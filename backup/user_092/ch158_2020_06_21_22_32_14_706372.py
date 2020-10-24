with open('texto.txt','r') as arquivo:
    cc = arquivo.read()
    L = cc.split()
    i = 0
    for e in L:
        i += len(e)
    print(i)
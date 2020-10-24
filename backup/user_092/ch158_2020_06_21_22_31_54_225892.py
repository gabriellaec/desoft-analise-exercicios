with open('texto.txt','r') as arquivo:
    cc = arquivo.read()
    L = cc.split()
    i = 0
    for e in range(len(L)):
        s = L[e]
        i += len(s)
    print(i)
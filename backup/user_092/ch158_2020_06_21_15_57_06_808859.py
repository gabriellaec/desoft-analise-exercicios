with open('texto.txt','r') as arquivo:
    cc = arquivo.read()
    n = cc.split()
    i = 0
    for e in range(len(n)):
        i += len(n[e])
        
    print(i)
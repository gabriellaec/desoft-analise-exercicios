with open('texto.txt','r') as arquivo:
    n = arquivo.split()
    i = 0
    for e in range(len(n)):
        i += len(n[e])
        
    print(i)
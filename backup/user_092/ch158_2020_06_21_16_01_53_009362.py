with open('texto.txt','r') as arquivo:
    conteudo_completo = arquivo.read()
    L = conteudo_completo.split()
    i = 0
    for e in range(len(L)):
        s = L[e]
        i += len(s[:])
        
    print(i)
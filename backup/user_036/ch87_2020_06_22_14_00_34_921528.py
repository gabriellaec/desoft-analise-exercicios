with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    s = 0
    for i in conteudo:
        s+= float(conteudo[1])*float(conteudo[2])
    print(s)
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    s = 0
    for i in conteudo:
        s+= conteudo[1]*conteudo[2]
    print(s)
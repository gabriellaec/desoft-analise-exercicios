with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    
    total = 0
    
    for p in conteudo[0]:
        total += p[1] * p[2]
    print (total)
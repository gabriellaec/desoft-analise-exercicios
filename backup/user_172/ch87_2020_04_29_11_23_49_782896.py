with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    y = 0
    for item in conteudo:
        x = item.split(',')
        y = y + x[1]*x[2]
        
print (y)
    
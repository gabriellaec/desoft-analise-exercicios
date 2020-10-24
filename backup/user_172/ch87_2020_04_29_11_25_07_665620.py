with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    y = 0
    for item in conteudo:
        x = item.split(',')
        a = int(x[1])
        b = int(x[2])
        y = y + a*b
        
print (y)
    
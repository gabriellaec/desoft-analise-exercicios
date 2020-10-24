with open('churras.txt', 'r') as arquivo:
    conteudo= arquivo.readlines()
preco= 0
cont= 0
for i in conteudo:
    coisas= i.split(',')
    preco += float(coisas[1])*float(coisas[2])
    
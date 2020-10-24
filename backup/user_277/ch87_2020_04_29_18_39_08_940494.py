with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    h=conteudo.split(',','\n')
for i in range(0,len(h)):
    
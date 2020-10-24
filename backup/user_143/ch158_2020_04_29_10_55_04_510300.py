with open ('texto.txt', 'r') as arquivo:
    conteudo= arquivo.read()
c=conteudo.split()
print (len(c))
    
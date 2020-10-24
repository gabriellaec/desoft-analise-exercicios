with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
splitted = conteudo.split(',')
print(splitted)
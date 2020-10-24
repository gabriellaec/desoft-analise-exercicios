with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
splitted = conteudo.split(',')
splitted = splitted.split('\n')
print(splitted)
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
virgula = conteudo.replace('
',',')
splitted = virgula.split(',')
print(splitted)
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
virgula = conteudo.replace('\n',',')
splitted = virgula.split(',')
print(splitted)
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
splitted = conteudo.split(',')
splitted2 = splitted.split('\n')
print(splitted2)
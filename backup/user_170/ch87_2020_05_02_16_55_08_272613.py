with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
splitted = conteudo.split(',' or '\n')
print(splitted)
for 
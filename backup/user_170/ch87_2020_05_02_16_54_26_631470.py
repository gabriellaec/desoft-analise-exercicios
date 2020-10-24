with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
splitted = conteudo.split(',' and '\n')
print(splitted)
with open('dados.csv', 'r') as arquivo:
    leitura = arquivo.read()
    palavras = leitura.split(',')

for i in range(len(palavras)):
    palavras[:-1] = '\t'
with open('dados.csv', 'r') as arquivo:
    conteudo=arquivo.read()
b=conteudo.replace(',', '\t')
print(b)
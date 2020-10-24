with open('dados.csv', 'r') as arquivo:
    conteudo=arquivo.read()
dados=conteudo.replace(',', '	')
with open('dados.tsv', 'w') as arquivo:
    arquivo.write(dados)
    

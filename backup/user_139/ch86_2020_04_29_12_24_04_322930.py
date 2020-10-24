while open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    return conteudo
while open('dados.tsv', 'a') as arquivo:
    arquivo.write("conteudo")
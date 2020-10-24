with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    return conteudo
with open('dados.tsv', 'a') as arquivo:
    arquivo.write("conteudo")
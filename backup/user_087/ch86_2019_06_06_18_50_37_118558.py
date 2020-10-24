with open ('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()

conteudo_novo = conteudo.replace(',','	')
with open('dados.tsv', 'w') as arquivo:
    arquivo.write(conteudo_novo)
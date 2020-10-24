with open('dados.csv','r') as arquivo:
    conteudo = arquivo.read()
    conteudo_tsv = conteudo.replace(',', '\t')

with open('dados.tsv','w') as arquivo:
    arquivo.write(conteudo_tsv)
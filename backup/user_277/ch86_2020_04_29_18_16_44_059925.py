with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    h=conteudo.replace(',','\t')
with open ('dados.tsv','w') as arquivo_2:
    arquivo_2.write(h)
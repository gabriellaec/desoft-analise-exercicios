with open ('dados.csv','r') as csv:
    conteudo = csv.read()
c = conteudo.split(',')
c1 = ('  ',join(c))
with open ('dados.tsv','r') as tsv:
    tsv.write(c1)


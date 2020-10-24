with open ('dados.csv','r') as csv:
    conteudo = csv.read()
c = conteudo.split(',')
c1 = ('  '.join(c))
with open ('dados.tsv','w') as tsv:
    tsv.write(c1)


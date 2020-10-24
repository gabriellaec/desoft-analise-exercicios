with open('dados.csv','r') as csv:
    conteudo = csv.read()
    semVirgula = conteudo.split(',')
    conteudo2 = ('	').join(semVirgula)

with open('dados.tsv','w') as tsv:
    tsv.write(conteudo2)
    
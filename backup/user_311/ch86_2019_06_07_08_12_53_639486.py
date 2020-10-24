with open('dados.csv','r') as csv:
    conteudo = csv.read()
    
t1 = conteudo.split(',')
t2 = ('	'.join(t1))

with open('dados.tsv','w') as tsv:
    tsv.write(t2)
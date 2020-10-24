with open('dados.csv','r') as arquivo:
    conteudo = arquivo.read().split(',')
x = conteudo[0]
for i in range(len(conteudo)-1 ):
    x += '\t' + conteudo[i+1]
with open('dados.tsv','w') as arquivo2:
    arquivo2.write(x)
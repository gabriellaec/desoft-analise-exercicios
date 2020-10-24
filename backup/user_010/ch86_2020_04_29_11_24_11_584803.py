with open ('dados.csv','r') as arquivo:
    conteudo=arquivo.read()

x=conteudo.split(',')
y='\t'.join (x)
print (y)

with open ('dados.tsv','w') as arquivo:
    arquivo.write (y)
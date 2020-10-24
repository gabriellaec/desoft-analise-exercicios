a1=open('dados.csv')
a2=open('dados.tsv','w')
for conteudo in a1.read():
	lista=conteudo.split(',')
	a2.write('	'.join(lista))
    
a1.close()
a2.close()
    
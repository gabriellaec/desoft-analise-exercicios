with open('dados.csv','r') as csv:
	texto= csv.read()
dados=[]
tx=texto.slpit()
x=0
for i in tx:
    dados.appen(i)
dados.join()
save dados as 'dados.tsv'
    
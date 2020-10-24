with open('dados.csv','r') as csv:
	texto= csv.read()
tx=(' '.join(texto))
with open('dados.tsv','w') as tsv:
    tsv.write(tx)
 
    
with open('dados.csv','r') as csv:
	t=csv.read()
    
	t2=t.replace(","," ")
with open('dados.tsv','w') as tsv:
    tsv.write(t2)